Role Name
=========

A role to deploy dqit webapp.

Requirements
------------

Requires roles java, tomcat which install those on the system.

Role Variables
--------------

See ./vars/main.yml and ./defaults/main.yml

Dependencies
------------

Depends on the java role.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: dqit