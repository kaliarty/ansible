firewall_setup
==============

This role uses information stored on hosts to configure their firewall.

Firewall rules should depend (only) on the roles that run on each given server. We would like to implement this in Ansible, but Ansible does not have a straithforward way to map roles to hosts:
this mapping is done by playbooks and can be dynamic. Only roles that actually run know where.

We solve this by doing the setup in two phases:
  - first, each role that install any listening servers stores info about listening ports on each server it runs on (using facts)
  - second, a role is run that converts those stored facts into a firewall configuration

This role implements the second phase. It is meant to be run on all hosts, and will configure their firewall.

We always allow incoming ssh connections.

By default, we allow ICMP messages (as they are required for proper network function, e. g. MTU Path Discovery).

Firewall-managing services `ufw` and `firewalld` are disabled by this role because they're unsupported (we might support them in the future). 
This role uses vanilla iptables and iptables persistence service to implement all its functionality.

For details of the implementation, see README.md of the `firewall_rules` role.

Requirements
------------

Requires `iptables`, which is already present, and `iptables-persistent` on Ubuntu and `iptables-services` on RHEL to persist firewall configuration.   

Role Variables
--------------

None

Dependencies
------------

No direct dependencies, but requires FW configuration to be stored on the hosts by firewall_rules role.

Example Playbook
----------------

This role is called automatically by firewall_rules.
