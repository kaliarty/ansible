node-exporter
=========

A role to deploy node-exporter.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

| Name                           | Description | Default |
| ------------------------------ |:----------- | ------- |
| `node_exporter_version`        | node-exporter version. | "{{ gen2_node_exporter_version }}" |
| `node_exporter_port `          | node-exporter listening port. | "9100" |
| `node_exporter_listen_address` | node-exporter listening address. | "0.0.0.0:{{ node_exporter_port }}" |
| `node_exporter_telemetry_path` | node-exporter telemetry path. | "/metrics" |
| `node_exporter_options`        | node-exporter run flags. | See [defaults/main.yml](./defaults/main.yml) |

Dependencies
------------

- prometheus_exporter

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: node_exporter
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
