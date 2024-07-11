ataccama-mmm-exporter
=========

A role to deploy ataccama-mmm-exporter.
This exporter is used to expose an MMM DB data as metrics.

Requirements
------------

Role installs all its requirements.

Role Variables
--------------

See defaults/main folder.

| Name                                 | Description | Default |
| ------------------------------------ |:----------- | ------- |
| `mmm_exporter_user`                  | System user for ataccama-mmm-exporter. | "postgres" |
| `mmm_exporter_group`                 | System group for ataccama-mmm-exporter user. | "{{ postgres_exporter_user }}" |
| `mmm_exporter_version`               | Version of ataccama-mmm-exporter package. | "0.10.0" |
| `mmm_exporter_home`                  | Home directory for ataccama-mmm-exporter user. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `mmm_exporter_datasource`            | The PostgreSQL server's data source to connect to. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `mmm_exporter_port`                  | ataccama-mmm-exporter listening port. | "9188" |
| `mmm_exporter_listen_address`        | ataccama-mmm-exporter listening address. | "0.0.0.0:{{ mmm_exporter_port }}" |
| `mmm_exporter_flags`                 | ataccama-mmm-exporter binary flags. | See [defaults/main/main.yml](./defaults/main/main.yml) |
| `mmm_exporter_queries_file`          | ataccama-mmm-exporter target queries file path. | "{{ postgres_exporter_home }}/queries.yml" |
| `mmm_exporter_queries`               | ataccama-mmm-exporter queries template. | "" |
| `mmm_exporter_additional_queries`    | Additional ataccama-mmm-exporter queries template. | "" |

Dependencies
------------

- prometheus_exporter

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: ataccama_mmm_exporter
          vars:
            mmm_exporter_queries: |-
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
