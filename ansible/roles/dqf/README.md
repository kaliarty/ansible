Role Name
=========

Data Quality Filter (DQF) module.

Added since version 14.5

Requirements
------------
- keycloak
- postgresql
- mmm backend

Role Variables
--------------
| name | default value                                                           |
|------|-------------------------------------------------------------------------|
| dqf_version | "{{ packages.dqf.version }}"                                            |
| dqf_install_dir | "{{ deployment_folder }}/{{ dqf_module_name }}"                         |
| dqf_package_download_type | "{{ packages.dqf.package_download_type \| default('maven_artifact') }}" |
| dqf_package_location | "{{ packages.dqf.package_location \| default ('') }}"                   |
| dqf_package_url | "{{ packages.dqf.package_url \| default ('') }}"                        |
| dqf_package_checksum | "{{ packages.dqf.package_checksum \| default(omit) }}"                  |
| dqf_service_user | dqf                                                                     |
| dqf_service_group | dqf                                                                     |
| dqf_database_name | dqf                                                                     |
| dqf_http_port | 8028                                                                    |
| dqf_grpc_port | 8528                                                                    |
| dqf_host | "{{ groups['dqf_server'][0] }}"                                                     |
| dqf_deployment_name |
| dqf_management_port | 8026                                                                    |
| dqf_java_heapdumps | "true"                                                                  |
| dqf_java_temp_folder | "{{ dqf_install_dir }}/tmp"                                             |

Dependencies
------------
- one_module

Example Playbook
----------------
See `one.yml`

License
-------
BSD

Author Information
------------------
An optional section for the role authors to include contact information, or a website (HTML is not allowed).
