Java
=========

A role to install AdoptOpenJDK Java

Role Variables
--------------

Set AdoptOpenJDK packages through
    
    adoptopenjdk_packages:
        - adoptopenjdk-11-hotspot
The first Java package in the list is set as system-wide default. 
The default value is `- adoptopenjdk-11-hotspot`

Dependencies
------------

`apt-transport-https` is needed on ubuntu and other debian based system 

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: java
           adoptopenjdk_packages: 
              - adoptopenjdk-11-hotspot
              - adoptopenjdk-8-hotspot
              
Installs AdoptOpenJDK 11 and 8, version 11 is set as system-wide default since it is first in the list. 