
firewall_rules
==============

Other roles call this role to request firewall rule instalation.

Firewall rules should depend (only) on the roles that run on each given server. We would like to implement this in Ansible, but Ansible does not have a straithforward way to map roles to hosts:
this mapping is done by playbooks and can be dynamic. Only roles that actually run know where.

We solve this by doing the setup in two phases:
  - first, each role that install any listening servers stores info about listening ports on each server it runs on (using facts)
  - second, a role is run that converts those stored facts into a firewall configuration

This role implements the infrastructure for the fist phase: it is meant to be called by other roles, and will persist its input on the target server.

Implementation details
----------------------

For decisions that lead to the current design, see [its proposal](https://www.notion.so/ataccama/Ansible-firewall-playbook-3f8210265ecd4ed998432e82c4561e1a).

`firewall_rules` does two main things: it stores value of the ruleset (passed in the `iptables` variable) on the target server, and calls firewall_setup to immediately update firewall.
`firewall_setup` then merges all currently present rulesets into one big ruleset and uses it to configure the firewall.

We implement this using dynamic facts: we store the rulesets as `/etc/ansible/facts.d/firewall/<ruleset_name>.in` and use a script `/etc/ansible/facts.d/firewall.fact` to merge them. (We use
the `.in` suffix so Ansible won't mistaken the incomplete files for facts.)

We have to choose the file name in such a way that separate roles won't overwrite each other's rulesets, but will rewrite its own. This is mostly solved by using `ansible_parent_role_paths`
to generate the file name - it works for every role that configures the firewall for itself, even when generic role is included by multiple specific roles. But it fails when a generic role
is called directly, as in the case of the `server` role: it is called multiple times directly in a playbook and it sets up multiple services, depending only on variables passed to it.
To handle this case, we allow directly setting the ruleset name using a variable. It is recommended to use the autogenerated name whenever possible.

The firewall_setup role disables all firewall managers (ufw and similar), enables iptables persistence, installs a fact script, refreshes facts and configures the firewall.
It applies the changes immediately (some roles check service availability using HTTP requests).

Deleting old rulesets must be handled separately, using a cleanup playbook. Note: this probably shouldn't be part of normal workflow, as clearing the rulesets will make next
firewall_setup deconfigure all rules except the ones it was called with, creating an outage.

WARNING: FIXME: when merging rulesets, dicts are merged and lists are appended (which should do the right thing), but other values are overriden. The order is stable but arbitrary
(currently alphabetical). Do not use different settings on a single server, or better yet: do not change them at all, the default should be OK.

Requirements
------------

none

Role Variables
--------------

iptables: see example for explanation.

firewall\_ruleset\_name: arbitrary name for the ruleset: must be unique for all roles on a given host. Default: colon-separated role include path (e. g. `one_module:rdm`)

Dependencies
------------

This role does not have any direct dependencies, but is useless without firewall_setup role that does the actual FW configuration.

Example Usage
----------------
Warning: packet logging is very resource-consuming. Even on lightly-loaded test environments, it could soft-lock the servers, making SSH connections impossible. Enable it
only with utmost care.

somerole/tasks/main.yml:

```
- name: install_some_software
    args: yes please

- include_role:
    name: firewall_rules
  vars:
    iptables:
      # Set to true to allow forwarding chain
      forwarding_allowed: false
      # specify if icmp/ping is allowed - filter table
      icmp_allowed: true
      # specify hosts from which is ping allowed
      icmp_allowed_from:
        - host: server
          ip: 1.2.3.4
      # specify tcp ports allowed (open) - filter table
      allowed_tcp_ports:
        - port: 80
        - port: 443
          source: 1.2.3.4                        # Optionally specify source address
          comment: "Some rule comment"           # Optional rule comment
      # specify other (non-tcp) ports allowed (open) - filter table
      allowed_ports:
        - port: 666
          protocol: udp
          source: 1.2.3.4                        # Optionally specify source address
          comment: "Some rule comment"           # Optional rule comment
      # configure additional custom chains
      chains:
        - name: "HTTP"
          comment: "http and https traffic"
          protocol: tcp                          # chain allowed ports protocol
          ports:                                 # chain allowed ports
            - 80
            - 443
        - name: "chain2"
          comment: "chain with limited source"
          protocol: tcp  # tcp/udp/...
          ports:
            - 6666
          sources:                               # limited only to this source
            - ip: someip
              host: somehost
      # Whether to log dropped packets
      log_dropped_packets: false
      # Log level for dropped packets
      log_dropped_packets_level: 4
      # Log rate limit for dropped packets
      log_drop_packets_limit: "1/s"
      # Log limit burst for dropped packets
      log_drop_packets_limit_burst: "10"
```

License
-------

internal

Author Information
------------------

This role is maintaned by Ataccama's Deployment team.
