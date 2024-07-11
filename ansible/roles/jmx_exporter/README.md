JMX Exporter
=========

A role to download and deploy configuration for JMX exporter for Prometheus.

Requirements
------------

No requirements

Role Variables
--------------

Role variables with their defaults are:

```yaml
jmx_exporter_version: 0.16.1
jmx_exporter_download_url: "https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/{{ jmx_exporter_version }}/jmx_prometheus_javaagent-{{ jmx_exporter_version }}.jar"

jmx_exporter_install_dir: /opt/jmx_exporter
jmx_exporter_config_dir: /opt/jmx_exporter/conf
jmx_exporter_config_template: jmx-prometheus-config.yml.j2
jmx_exporter_jar: jmx_prometheus_javaagent.jar
```

Dependencies
------------

No dependency

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }
