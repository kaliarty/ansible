# Release notes for One20 Ansible

## 14.1.0

This release removes the configuration service and adds three new services. It also contains various bug fixes.

### Note about version

Please note, this version supports only 14.x version.

### New features

* Configuration service was removed. The remaining functionality (DPE management) is now part of DPM service.
* Three new services were added:
  * Comment
  * Task
  * Workflow

### Bugs fixed

There are  multiple example inventories fixes, see CHANGELOG.md for details.

## 13.9.0

This Ansible release contains Ataccama Gen2 v13.9 LTS.

### New features
* Replaced ElasticSearch with Opensearch
* Replaced Kibana with OpenSearch Dashboards
  * please note: kibana.<domain_name> hostname is preserved in this release

### Bug fixed
* Fixed various bugs in the Ansible code

### Improvements
* monitoring labels
* SMTP false logs suppression

### Other changes
* since version 13.8 there is required authentification for downloading content packs from S3, see docs/inventory.md file for details please
* 3rd parties upgrades, see CHANGELOG.md

### Fix: service home directories

Due to historical reasons, few of services have wrongly set home directory parameter. To fix it using Ansible, you have to stop all affected services to be able run Ansible without an issue. Those services are:
* monitoring and dependency server
  * `elasticsearch_exporter.service`
* dependency server
  * `keycloak-server.service`
  * `minio-storage.service`
  * `MantaFlowServer.service`
  * `MantaUtilityTool.service`

Each service must be stopped on remote server using sudo (e.g. `keycloak-server`):
```
systemctl stop keycloak-server
```

We implemented a limited self-healing functionality, because broken (stopped) Keycloak server can dissallow to use whole platform. All services should come back online by itself within seconds after the Keycloak server. To be completely sure, check the monitoring after the sucessful Ansbile run to see if all components are running. Restart any that do not.

## 13.8.0

### Breaking change: content management
A new way of content management for MMM was introduced in 13.8.0. For that, one has to set and configure the `mmm_content_packs` and `mmm_content_pack_s3_repositories` variables in the inventory prior to the installation.
See the commented configuration example in the example inventories for reference.

## 13.5.0-1

This release includes Elasticsearch version update due to log4shell issue. Also there is an update of td-agent version.

## 13.5.0

This release contains new features as well as other improvements and bug fixes. Since this release, the RELEASENOTES.md file contains detailed information about changes made. It also contains workarounds and steps necessary for a successful upgrade, if any.

### Doc: Ansible documentation in PDF format

Ansible documentation, which is located in the doc directory is also rendered into PDF format, which can be easily readable instead of raw text from MD files. You can find it in the doc directory, file called `documentation.pdf`.

### Fix: Keycloak server heap size

There is bug in Keycloak service unit file. Heap size parameter is ignored and set to default value 512MB which is small and causes Keycloak server outages. Fix is implemented in this release, but it can be fixed manually:

* Log into dependency server
* remove following line from file `/etc/systemd/system/keycloak-server.service`
```
Environment="LAUNCH_JBOSS_IN_BACKGROUND=1 JBOSS_PIDFILE='/var/tmp/keycloak.pid' JAVA_OPTS='-Xms512m -Xmx2048m -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true'"
```
* create directory `/etc/systemd/system/keycloak-server.service.d`
```
sudo mkdir /etc/systemd/system/keycloak-server.service.d
```
* create file `/etc/systemd/system/keycloak-server.service.d/keyloak-server.conf` with following content:
```
[Service]
Environment="JAVA_OPTS=-Xms512m -Xmx2048m -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true"
Environment="LAUNCH_JBOSS_IN_BACKGROUND=1"
Environment="JBOSS_PIDFILE=/var/tmp/keycloak.pid"
```
* reload service unit configuration
```
sudo systemctl daemon-reload
```
* stop Keycloak server
```
sudo systemctl stop keycloak-server
```
* start Keycloak server
```
sudo systemctl start keycloak-server
```
* check running processes if Keycloak server is running with properly set javaheap size, e.g. (please, note parameter -Xmx2048m):
```
keycloak  687774  320  4.3 3556092 709188 ?      Sl   09:41   0:25  \_ java -D[Standalone] -server -Xms512m -Xmx2048m -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true --add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED --add-exports=jdk.unsupported/sun.reflect=ALL-UNNAMED -Dorg.jboss.boot.log.file=/opt/keycloak/keycloak/standalone/log/server.log -Dlogging.configuration=file:/opt/keycloak/keycloak/standalone/configuration/logging.properties -jar /opt/keycloak/keycloak/jboss-modules.jar -mp /opt/keycloak/keycloak/modules org.jboss.as.standalone -Djboss.home.dir=/opt/keycloak/keycloak -Djboss.server.base.dir=/opt/keycloak/keycloak/standalone -Djboss.http.port=8080 -Dkeycloak.profile.feature.token_exchange=enabled -b 0.0.0.0 -Dkeycloak.migration.action=import -Dkeycloak.migration.provider=singleFile -Dkeycloak.migration.realmName=ataccamaone -Dkeycloak.migration.file=/opt/keycloak/realms/ataccamaone.json -Dkeycloak.migration.strategy=IGNORE_EXISTING

```
