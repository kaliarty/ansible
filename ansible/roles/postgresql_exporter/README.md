postgres-exporter
=========

A role to deploy postgres-exporter.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

See defaults/main folder.

| Name                                      | Description | Default |
| ----------------------------------------- |:----------- | ------- |
| `postgres_exporter_user`                  | System user for postgres-exporter. | "postgres" |
| `postgres_exporter_group`                 | System group for postgres-exporter user. | "{{ postgres_exporter_user }}" |
| `postgres_exporter_version`               | Version of postgres-exporter package. | "0.10.0" |
| `postgres_exporter_home`                  | Home directory for postgres-exporter user. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `postgres_exporter_datasource`            | The PostgreSQL server's data source to connect to. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `postgres_exporter_port`                  | postgres-exporter listening port. | "9187" |
| `postgres_exporter_listen_address`        | postgres-exporter listening address. | "0.0.0.0:{{ postgres_exporter_port }}" |
| `postgres_exporter_flags`                 | postgres-exporter binary flags. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `postgres_exporter_queries_file`          | postgres-exporter target queries file path. | "{{ postgres_exporter_home }}/queries.yml" |
| `postgres_exporter_queries`               | postgres-exporter queries template. | See [defaults/main/queries.yml](./defaults/main/queries.yml) |
| `postgres_exporter_additional_queries`    | Additional postgres-exporter queries template. | "" |

Dependencies
------------

- prometheus_exporter

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: postgresql_exporter
          vars:
            postgres_exporter_additional_queries: |-
              {%- if 'server01' in group_names %}
              {{ lookup('file', '/tmp/queries.yml') }}
              {%- else -%}
              {%- endif %}
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
