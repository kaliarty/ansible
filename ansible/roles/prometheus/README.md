Prometheus
=========

Role that configures community role to deploy Prometheus monitoring server and Prometheus Alertmanager.  

Requirements
------------

Requires the following roles: 

    - https://github.com/cloudalchemy/ansible-prometheus
    - https://github.com/cloudalchemy/ansible-alertmanager

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

Depends on the roles mentioned above

Example Playbook
----------------

    - hosts: servers
      roles:
         - prometheus
