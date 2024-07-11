ONE module deploy
=========

A role to deploy, configure and start ONE 2.0 module using zip packages using different ways

Requirements
------------

For running the module, Java is required to be installed previously on the machine.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

Requires Java,

Role Variables
--------------

vars:
```yaml
package_download_folder: /var/tmp
package_version: "{{ package_versions.dpm }}"
package_url_type: "{{ dpm_package_url_type }}" # maven_artifact or anything_elase
package_url: "{{ package_urls.dpm.url }}" # not valid for maven_artifact
service_name: dpm # systemd unit
service_user: "{{ dpm_service_user }}"
service_group: "{{ dpm_service_group }}"
service_env:
  SPRING_DATASOURCE_URL: "jdbc:postgresql://{{ postgres.host }}:{{ postgres.port }}/{{ dpm.database_name }}{{ postgres.postgresql_server.parameters | default( '' ) }}"
  java_opts:
enable_java_heapdumps: "false"
java_heapdump_context_dir: "{{ install_dir }}/{{ module_name }}"
java_heapdump_dir: "{{ java_heapdump_context_dir }}/tmp/heapdump"
```
If heap dumps shoud be enabled caller of the ONE module should make sure to use `java_opts` property to specify `JAVA_OPTS` environment variable value. This way one_module is able to append heap dump enabling parameters.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
- hosts: servers
  roles:
     - { role: username.rolename, x: 42 }
```
