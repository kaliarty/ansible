CA - add to truststores
============

Role for copying CA to the system and java ca truststores.

Requirements
------------

The role installs all its requirements.

Role Variables
--------------

The defaults are in [defaults/main.yml](./defaults/main.yml).
See also variables in **vars/** folder.

Dependencies
------------

All dependencies for this role are specified in **roles/requirements.yml**.

Example Playbook
----------------

```yaml
- hosts: all
  any_errors_fatal: true
  roles:
    - role: ca_add_to_truststores
```

License
-------

Internal

Author Information
------------------
