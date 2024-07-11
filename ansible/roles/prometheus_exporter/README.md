prometheus-exporters
=========

A base role to deploy prometheus-exporters.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

| Name                                      | Description | Required | Default                               |
| ----------------------------------------- |:----------- | -------- |---------------------------------------|
| `prometheus_exporter_name`                | Name of prometheus-exporter. | yes | -                                     |
| `prometheus_exporter_user`                | System user for prometheus-exporter. | no | "prometheus"                          |
| `prometheus_exporter_user_manage`         | Enable or disable system user creation. | no | false                                 |
| `prometheus_exporter_group`               | System group for prometheus-exporter user. | no | "{{ prometheus_exporter_user }}"      |
| `prometheus_exporter_group_manage`        | Enable or disable system group creation. | no | false                                 |
| `prometheus_exporters_dir`                | Directory in which Prometheus exporters are or should be installed. | no | "/opt/prometheus/exporters"           |
| `prometheus_exporters_dist_dir`           | Directory in which current exporter should be installed. | no | "{{ prometheus_exporters_dir }}/dist" |
| `prometheus_exporter_create_dist`         | Create dist directory for the exporter. | no | false                                 |
| `prometheus_exporter_download_url`        | Download url of postgres-exporter package. | yes | -                                     |
| `prometheus_exporter_dist`                | prometheus-exporter package name. | yes | -                                     |
| `prometheus_exporter_bin`                 | prometheus-exporter binary path. | yes | -                                     |
| `prometheus_exporter_home`                | Home directory for prometheus-exporter user. | no | "/home/prometheus"                    |
| `prometheus_exporter_home_manage`         | Enable or disable home directory creation. | no | true                              |
| `prometheus_exporter_config_file`         | Environment variables file path for prometheus-exporter systemd unit. | no | ""                                    |
| `prometheus_exporter_env_variables`       | Environment variables for prometheus-exporter systemd unit. | no | {}                                    |
| `prometheus_exporter_service_name`        | prometheus-exporter systemd unit name. | yes | -                                     |
| `prometheus_exporter_service_execstart`   | Systemd unit ExecStart. | yes | -                                     |
| `prometheus_exporter_service_execstop`    | Systemd unit ExecStop. | no | ""                                    |
| `prometheus_exporter_service_execreload`  | Systemd unit ExecReload. | no | ""                                    |
| `prometheus_exporter_log_path`            | prometheus-exporter logs path. | no | ""                                    |
| `prometheus_exporter_service_description` | Systemd unit description. | no | ""                                    |
| `prometheus_exporter_service_type`        | Systemd unit service type. | no | "simple"                              |
| `prometheus_exporter_service_restart_sec` | Systemd unit RestartSec. | no | "100ms"                               |
| `prometheus_exporter_service_private_tmp` | Systemd unit PrivateTmp. | no | false                                 |

Dependencies
------------

- 0x0i.systemd

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: prometheus_exporter
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
