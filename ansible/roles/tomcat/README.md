Tomcat
=========

A role to install and configure Apache Tomcat on the server. Taken from https://github.com/robertdebock/ansible-role-tomcat, and modified it, to fix some issues and problems it has:
- not working well with updates
- no monitoring set up
- fully doesn't work with Ansible 2.9
- not idempotent
- cannot import webapp directories

This attempt fixes those issues.

Requirements
------------

Requires java on the machine to be present. Other dependencies are also installed.

Role Variables
--------------

See defaults/main.yml

Dependencies
------------

Depends on java

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: tomcat
