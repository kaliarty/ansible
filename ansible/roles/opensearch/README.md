Opensearch
=========

A role to install and configure OpenSearch - an open source search engine.

Requirements
------------

This role has no requirements. OpenSearch is bundled with its own JDK, in the case different version of Java is desired, consumers of this role should install it on their own.

Role Variables
--------------

Some default role variables are

| Name                          | Description                                             | Default                              |
|-------------------------------|---------------------------------------------------------|--------------------------------------|
| `opensearch_version`          | Version of OpenSearch installed                         | `2.1.0`                              |
| `opensearch_download_dir`     | Directory, in which is the OpenSearch binary downloaded | `/var/tmp`                           |
| `opensearch_install_dir`      | Directory, in which is the OpenSearch installed         | `/usr/share/opensearch`              |
| `opensearch_config_dir`       | Configuration directory for OpenSearch                  | `/usr/share/opensearch/config`       |
| `opensearch_log_dir`          | OpenSearch log directory location                       | `/var/log/opensearch`                |
| `opensearch_data_dirs`        | OpenSearch data directories location (list)             | `[/var/lib/opensearch]`              |
| `opensearch_pid_file`         | Path to the OpenSearch PID file                         | `/var/run/opensearch/opensearch.pid` |
| `opensearch_system_user`      | OpenSearch system user name                             | `opensearch`                         |
| `opensearch_vm_max_map_count` | Linux kernel `vm.max_map_count` setting                 | `262144`                             |
| `opensearch_fs_file_max`      | Limit for number of opened files by OpenSearch          | `65536`                              |
| `opensearch_proc_max`         | Limit for number of spawned processes by OpenSearch     | `4096`                               |
| `opensearch_cluster_name`     | OpenSearch Cluster name                                 | `default`                            |
| `opensearch_cluster_type`     | single-node / cluster                                   | `single-node`                        |
| `opensearch_api_port`         | OpenSearch API port                                     | `9200`                               |
| `opensearch_transport_port`   | OpenSearch transport port                               | `9301`                               |
| `opensearch_xms`              | Xms value for OpenSearch JVM                            | `2g`                                 |
| `opensearch_xmx`              | Xmx value for OpenSearch JVM                            | `2g`                                 |
| `opensearch_security_enabled` | Whether to enable security features for OpenSearch      | `false`                              |
| `opensearch_plugins`          | List of OpenSearch plugins to be installed              | `[]`                                 |
| `opensearch_config`           | Additional OpenSearch YAML configuration                | `{}`                                 |
| `opensearch_ism_policies`     | List of OpenSearch ISM policies to be configured        | `[]`                                 |
| `opensearch_index_templates`  | List of OpenSearch Index templates to be configured     | `[]`                                 |

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
    - role: opensearch
```

License
-------

Internal

Author Information
------------------

