Role Name
=========

Ataccama Ansible role to deploy chrony.

chrony
======

`Chrony` is a flexible implementation of the Network Time Protocol (NTP). It is used to synchronize the system clock from different NTP servers, reference clocks or via manual input.

`chronyd` is a daemon for synchronisation of the system clock. It can synchronise the clock with NTP servers, reference clocks, and manual input using wristwatch and keyboard via chronyc. 

Requirements
------------

This role is limited to

* CentOS 8  
* CentOS 7
* RHEL 8
* Ubuntu 20.04 - Focal
* Ubuntu 18.04 - Bionic
* Ubuntu 16.04 - Xenial


Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

* `ntp_enabled` --- If enabled is true so the ntp playbook will be running in the whole deployment, If enabled is false so the ntp playbook will be skipped in case the customer already configured NTP on all server, default `true`
* `chrony_disable_ntpd` --- disable the old NTP daemon, default `true`
* `chrony_enable` --- enable `chrony` NTP daemon, default `true`
* `chrony_ntp_servers` --- list of NTP servers in use, default `['0.pool.ntp.org', '1.pool.ntp.org', '2.pool.ntp.org', '3.pool.ntp.org']`
* `chrony_timezone` --- timezone for the system. Run `timedatectl list-timezones` on any systemd system to list available timezones, default `UTC`


Variables path
--------------

Put the variables under .../group_vars/all/vars.yml as follows:

```
ntp_enabled: true
chrony_ntp_servers: 
  - "192.168.23.3 iburst"
  - "1.ubuntu.pool.ntp.org iburst"
  - "10.0.0.1 iburst"
chrony_timezone: "UTC"
chrony_disable_ntpd: true
chrony_enable: true
```


Dependencies
------------
None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - chrony

