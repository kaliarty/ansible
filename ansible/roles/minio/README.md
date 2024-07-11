MinIO
=========

Install and configure the Minio S3 compatible object storage server on RHEL/CentOS and Debian/Ubuntu.

Requirements
------------

Requires 0x0i.systemd role from Ansible Galaxy.

Role Variables
--------------

See defaults/main.yml

Dependencies
------------

Requires 0x0i.systemd role from Ansible Galaxy.

Example Playbook
----------------

    - hosts: servers
      roles:
         - minio
