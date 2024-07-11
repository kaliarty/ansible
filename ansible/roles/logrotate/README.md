Logrotate
=========

The role installs logrotate on a target host.

Requirements
------------

The role installs all its requirements.

Role Variables
--------------

Variables of [defaults/main.yml](./defaults/main.yml):

| Name | Description | Default | Required |
| ---- | ----------- | ------- | -------- |
| `logrotate_filename` | The name of the target logrotate file | `` | yes |
| `log_paths` | The list of log files to handle | `` | yes |
| `logrotate_options` | Logrotate options that will be written to the target logrotate file | See [defaults/main.yml](./defaults/main.yml) | no |

Dependencies
------------

All dependencies for this role are specified in **roles/requirements.yml**.

Example Playbook
----------------

```yaml
- hosts: all
  any_errors_fatal: true
  roles:
    - role: logrotate
      vars:
        logrotate_filename: test
        log_paths:
          - /var/log/test/*
```

License
-------

Internal

Author Information
------------------
