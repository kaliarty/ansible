Opensearch Dashboards
=========

A role to install and configure OpenSearch Dashboards - a visualization tool for data in OpenSearch.

Requirements
------------

This role has no requirements.

Role Variables
--------------

Some default role variables are

| Name                                     | Description                                                        | Default                                   |
|------------------------------------------|--------------------------------------------------------------------|-------------------------------------------|
| `opensearch_dashboards_version`          | Version of OpenSearch Dashboards installed                         | `2.1.0`                                   |
| `opensearch_dashboards_download_dir`     | Directory, in which is the OpenSearch Dashboards binary downloaded | `/var/tmp`                                |
| `opensearch_dashboards_install_dir`      | Directory, in which is the OpenSearch Dashboards installed         | `/usr/share/opensearch-dashboards`        |
| `opensearch_dashboards_config_dir`       | Configuration directory for OpenSearch Dashboards                  | `/usr/share/opensearch-dashboards/config` |
| `opensearch_dashboards_data_dir`         | OpenSearch Dashboards data directory                               | `/var/lib/opensearch-dashboards`          |
| `opensearch_dashboards_system_user`      | OpenSearch Dashboards system user name                             | `opensearch-dashboards`                   |
| `opensearch_dashboards fs_file_max`      | Limit for number of opened files by OpenSearch Dashboards          | `65536`                                   |
| `opensearch_dashboards_proc_max`         | Limit for number of spawned processes by OpenSearch Dashboards     | `4096`                                    |
| `opensearch_dashboards_server_port`      | OpenSearch Dashboards server port                                  | `5601`                                    |
| `opensearch_hosts`                       | List of OpenSearch nodes that Dashboards connect to                | `[]`                                      |
| `opensearch_dashboards_security_enabled` | Whether to enable security features for OpenSearch Dashboards      | `false`                                   |
| `opensearch_dashboards_plugins`          | List of OpenSearch Dashboards plugins to be installed              | `[]`                                      |
| `opensearch_dashboards_config`           | Additional OpenSearch Dashboards yaml configuration                | `{}`                                      |

See [defaults/main.yml](./defaults/main.yml) for the complete reference.

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```yaml
- hosts: all
  any_errors_fatal: true
  roles:
    - role: opensearch_dashboards
```

License
-------

Internal
