nginx-exporter
=========

A role to deploy nginx-exporter.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

| Name                            | Description | Default |
| ------------------------------- |:----------- | ------- |
| `nginx_exporter_version`        | nginx-exporter version. | "{{ gen2_nginx_exporter_version }}" |
| `nginx_exporter_port`           | nginx-exporter listening port. | "9113" |
| `nginx_exporter_listen_address` | nginx-exporter listening address. | ":{{ nginx_exporter_port }}" |
| `nginx_scrape_uri`              | nginx stab status uri. | "`http://127.0.0.1:8001/nginx_status`" |
| `nginx_exporter_options`        | nginx-exporter run flags. | See [defaults/main.yml](./defaults/main.yml) |

Dependencies
------------

- prometheus_exporter

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: nginx_exporter
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
