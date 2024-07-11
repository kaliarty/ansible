PostreSql role for Azure and AWS managed PostgreSql
============

Ataccama role for deployment and setup of Azure or AWS managed PostgreSql for Ataccama product (database, schemas, users...).

Requirements
------------

Collections:
    - community.postgresql

Role Variables
--------------

Example of server variables:

```
mdm:
  postgresql_server:
    hostname: "{{ database_host_mdm }}"
    admin_user: "{{ postgresql_admin_user }}"
    admin_password: "{{ postgresql_admin_password }}"
    parameters: "?sslmode=require&amp;gssEncMode=disable"
    users:
      - name: mdm
        password: mdm
        role_attr_flags: CREATEDB,CREATEROLE,NOSUPERUSER,INHERIT,LOGIN
    databases:
      - name: mdc_db
        owner: mdm
      - name: it_db
        owner: mdm
      - name: esb_db
        owner: mdm
      - name: mda_cache
        owner: mdm
      - name: external
        owner: mdm
      - name: log_db
        owner: mdm
      - name: eh_db
        owner: mdm
```

Dependencies
------------

-

Example Playbook
----------------

- hosts: bastion
  collections:
    - community.postgresql
  roles:
    - postgresql_cloud
