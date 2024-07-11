monitoring_rules
=========

Other roles (dynamically) include `monitoring_rules` to ensure given endpoints are being monitored by Prometheus.

This role is passed a ruleset (see below) in the `monitoring_ruleset` var. It fills in missing parameters and then stores the ruleset on monitoring server(s) as dynamic facts. It then calls `prometheus` role to read the facts and update Prometheus config accordingly.

The name of the file stored on monitoing server should correspond to the service being monitored and must be static and unique to each service
(to ensure it is properly overwritten when demands change, and that multiple services won't overwrite each other's rules).
This part of the name can be overriden using `monitoring_ruleset_name` variable. It defaults to the colon-separated list of parent roles.
`monitoring_rules` prepends then the name of the calling host to it, as some services are installed to multiple hosts.

The ruleset is a dict, or a list of such dicts, each identical to an item of prometheus' `scrape_config` (let's call it 'rule'), with following exceptions:
  - If `job_name` is ommited, the `monitoring_ruleset_name` (if given) or the calling role's name (i. e. the first item of `ansible_parent_role_names`) is substituted.
  - If `static_configs` is omitted, a single empty item is substituted (and immediately filled in as decribed below).
  - If an item of `static_configs` does not contain any `targets`, a single target is generated as follows:
    - target hostname is the name of calling host
    - target port is looked up in the rule, under a `port` key
These rules mean that in the most common case when a role is setting up a monitoring targetting its own server, under its own name, it is enough to specify `metrics_path` and `port`: all remaining values are properly generated.

The `prometheus` role is expected to merge rulesets with the same `job_name` under a single job (Prometheus doesn't allow duplicate names)
by concatenating their targets. When multiple rules with the same name differ in key other than `targets`, the result s unspecified
(currently, it will be overwritten in arbitrary order).

High Availability: this role configures all servers in `monitoring_server_list` to have the same configuration.

Requirements
------------

Python 3, Ansible >= 4.5 (possibly lower; we did not try to pinpoint the specific version).

The reason of Ansible version requirement is that Ansible 2.10 contains a bug where a role that uses `with_first_found` that is delegated
doesn't search all paths for files. This breaks cloudalchemy.prometheus role that we depend on.

Role Variables
--------------

- `monitoring_server_list`: list of servers where Prometheus should be configured. Default to `groups.monitoring`.
- `monitoring_ruleset_name`: name used as part of the stored ruleset file name, and as default value for monitoring job name.
- `monitoring_ruleset`: a dict or list of dicts describing what will be monitored. See description.

Dependencies
------------

Depends on specific behaviour of `prometheus` role (see descrption).

Example
----------------

Simple configuration: monitor current host:

```yaml
- name: set monitoring rules
  include_role:
    name: monitoring_rules
  vars:
    monitoring_ruleset:
      metrics_path: "/auth/realms/master/metrics"
      port: "{{ keycloak_port }}"
```

More complicated example: a role that (depending on its configuration) installs various services that require authentization:

```yaml
- name: set monitoring rules
  include_role:
    name: monitoring_rules
  tags: monitoring
  vars:
    monitoring_ruleset_name: "{{ server_instance }}-server"
    monitoring_ruleset:
      metrics_path: /actuator/prometheus/
      basic_auth:
        username: "{{ keycloak_monitoring_user.username }}"
        password: "{{ keycloak_monitoring_user.password }}"
      scheme: http
      port: "{{ jmx.port }}"
```

License
-------

internal

Author Information
------------------

t_deployment
