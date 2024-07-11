Postgres
=========

Ataccama wrapper role for Postgres Database deployment and setup for Ataccama product. Wraps a Postgres community role from Galaxy. Works both with Debian and Redhat based systems.

Requirements
------------
This role requires Ansible in version 2.8+

Requires the dependency role https://github.com/geerlingguy/ansible-role-postgresql

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Available variables are listed below (see defaults/main.yml):

```
postgresql_user: postgres
postgresql_group: postgres
```
User and group name for running PosgreSQL server.


```
postgresql_python_library: python3-psycopg2
```
Required python library.


```
postgresql_databases: []
```
A list of databases which is created on the DB server(s). Each entry will create separate database with name `name`. See file `defaults/main.yml` for available database options.


```
postgresql_users: []
```
A list of database users.

```
default_postgresql_conf: []
```
Additional list of database server settings.

```
default_pg_hba_conf:
  - { type: local, database: all, user: postgres, auth_method: peer }
  - { type: local, database: all, user: all, auth_method: peer }
  - { type: host, database: all, user: all, address: '127.0.0.1/32', auth_method: md5 }
  - { type: host, database: all, user: all, address: '::1/128', auth_method: md5 }
```
Database server `pg_hba.conf` file (ACL).


```
postgres_users_no_log: false
```
Whether to output user data when managing users.

:information_source: Please note, there are more variables which can be overriden. For details see `defaults/main.yml` file from dependency role.

Dependencies
------------
Depends (imports) on the Postgres role from Galaxy https://github.com/geerlingguy/ansible-role-postgresql
