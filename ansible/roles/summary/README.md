
summary
==============

Other roles call this role to store a summary of the work done.

These sumaries are picked by `print_summary` role later and formatted as a nice result.

Implementation details
----------------------

Requirements
------------

Tag all calls to `summary` role with a `summary` tag. Also apply this tag to all prerequisites (`set_fact` and similar). This is necessary to allow users to generate sumary without before installing the whole platform.

Role Variables
--------------

group: all summaries with the same group will be printed as a list, using the `group` as a heading. Does have nothing to do with UNIX groups. Use `Platform` for ONE modules etc., `Prometheus exporters` for exporters etc.

summary: the value of the summary. Summaries are arbitrary dicts (must be JSON-serializable); we are using a convention to keep them uniform. See below, also example.

summary.name: when set, it will be used and formated as a heading. Use whenever possible.

summary.details: we generate two reports: full and shortened. The shortened one omits the `details` key from all dicts and subdicts. The intent is that the shortened report contains information that interests *users*, while the full report is of interest to *system adminitrators*. Details should contain info such as internal users, install directories etc.

summary_name: arbitrary name for the summary: must be unique for all roles on a given host. Default: colon-separated role include path (e. g. `one_module:rdm`). Used as a filename when storing the summary.

Dependencies
------------


Example Usage
----------------

TODO

somerole/tasks/main.yml:

```
- name: Store a summary
  include_role:
    name: summary
  vars:
    group: Platform
    summary:
      name: DQIT
      description: "Ataccama platform module: data quality issue tracker"
      version: "{{ package_version }}"
      details:
        directories: "{{ [ dqit_install_dir ] }}"
        os_user: "{{ dqit_service_user }}"
        os_group: "{{ dqit_service_group }}"
        services: "{{ ['dqit'] }}"
        tomcat_users:
          - username: admin
            password: admin
            roles:
              - user
              - supervisor
              - admin
          - username: user
            password: user
            roles:
              - user
          - username: dqit
            password: dqit
            roles:
              - user
              - supervisor
              - admin
          - username: super
            password: super
            roles:
              - user
              - supervisor
  tags: summary
```

License
-------

internal

Author Information
------------------

This role is maintaned by Ataccama's Deployment team.
