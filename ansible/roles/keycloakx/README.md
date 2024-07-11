KeyCloakX
=========

A role to deploy an instance of Ataccama build of KeyCloakX server

Role Variables
--------------

See defaults/main.yml and vars/main.yml. Example of using the role is in playbook `dependencies.yml`.

Dependencies
------------

Java needs to be installed on the system.
HTTP proxy service with TLS termination is expected.

Example Playbook
----------------

Example of how to use your role:

    - role: keycloakx
      vars:
        keycloak_config:
          proxy: edge
          hostname: "{{ nginx_hosts.one.hostname }}"
          cache-stack: tcp
          db-url-host: "{{ postgres.host }}"
          db-username: "{{ postgres.database.owner }}"
          db-password: "{{ postgres.database.password }}"
          db-url-port: "{{ postgres.port }}"
          db-url-database: "{{ keycloak.database_name }}"

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
