process-exporter
=========

A role to deploy process-exporter.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

| Name                                     | Description | Default |
| ---------------------------------------- |:----------- | ------- |
| `process_exporter_version`               | process-exporter version. | "{{ gen2_process_exporter_version }}" |
| `process_exporter_port`                  | process-exporter listening port. | "9256" |
| `process_exporter_listen_address`        | process-exporter listening address. | "0.0.0.0:{{ process_exporter_port }}" |
| `process_exporter_config_dir`            | Directory where processes config will be installed. | "/etc/process_exporter" |
| `process_exporter_processes_config_file` | Processes config file. | "{{ process_exporter_config_dir }}/config.yml" |
| `process_exporter_options`               | process-exporter run flags. | See [defaults/main.yml](./defaults/main.yml) |

Dependencies
------------

- prometheus_exporter

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: process_exporter
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
