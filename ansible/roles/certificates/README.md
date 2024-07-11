Certificates
============

Role for management of TLS certificates for one2.0 platform.

Requirements
------------

  collections:
    - community.crypto.openssl_certificate
    - community.crypto.openssl_csr
    - community.crypto.openssl_privatekey

Role Variables
--------------

certnames (array) - list of certificate 'common names'. Every name = pair of key and certificate.
role has default 3 certificates for ONE2.0 deployment

Dependencies
------------
python cryptography, see main.yml

Example Playbook
----------------

- hosts: proxies
  collections:
    - community.crypto.openssl_certificate
    - community.crypto.openssl_csr
    - community.crypto.openssl_privatekey
  roles:
    - certificates
