<a name="14.5.2-1"></a>
# 14.5.2-1 (2024/02/27)


## Bug Fixes

* **gen2** updated version of the platform modules
   * mdm
   * mdm-server
   * rdm
   * mmm-be
   * server
<a name="14.5.2"></a>
# 14.5.2 (2024/02/20)


## Features

* **gen2** bump business version to 14.5.2 for modules
  * mmm-be
  * server
  * mdm
  * mdm-server
<a name="14.5.1"></a>
# 14.5.1 (2023/12/19)


## Bug Fixes

* **DQF:**
  * add missing database for cloud managed db
  * install missing uuid-ossp extension
* **mde:** added encryption key files
* **comment:** temporarily fix of service configuration
* **mdm:** fix db properties
* **mdm-webapp:** using secret for client_id
* **monitoring:** fixed prometheus targets
<a name="14.5.0-4"></a>
# 14.5.0-4 (2023/11/03)


## Bug Fixes

* `slack_proxy_url` is now undefined by default
* **dqf:** increase max file size on nginx proxy to 50MB
* **mdm:** fix db properties in `application.properties` file
* **mmm:** increase default heap size to 3500MB

<a name="14.5.0-3"></a>
# 14.5.0-3 (2023/10/23)


## Bug Fixes

* **security:** remove default secrets from package

<a name="14.5.0-2"></a>
# 14.5.0-2 (2023/10/13)


## Bug Fixes

* optional slack plugin
* **mdm-webapp** using secret for client id
* **databases**
  * add missing DQF database
  * install missing uuid-ossp extension for mde

<a name="14.5.0-1"></a>
# 14.5.0-1 (2023/10/05)


## Bug Fixes

* **example inventories** align cert and key names
* **mde** fix default variables names
* **tomcat** bump version to 9.0.80
* **rdm**  use correct module name for dpe
<a name="14.5.0"></a>
## 14.5.0 (2023/09/26)


## Bug Fixes

* **mdm:** port changes in MDM/RDM
* **monitoring:** keycloak auth for comment service
* **term-suggestion** fix env PATH for python based services
* **fluentbit:** use https connection for yum repo

## Features

* **dqf:** add data quality firewall module
* **mde:** add mde_lineage module
* **keycloakx:** upgrade to 21.0.1-4
* **nginx:** check if nginx service started up
<a name="14.4.0"></a>
## 14.4.0 (2023/06/26)


## Bug Fixes

* **mdm:** application.properties - admin client needs to be enabled for kc health check
* **mmm:** add mmm-backend notification channel base url
* **rhel8:** fix adoptium repository key import
* **java** default java set to adoptiumopenjdk
* use consistent name scheme for generated DMM-JWK

## Features

* **monitoring:** make prometheus alerts optional
<a name="14.3.0-1"></a>
## 14.3.0-1 (2023/05/11)


## Bug Fixes

* **frontend:**
  * added startup-wait property
  * posthog disabled by default
* **firewall:** fixed for installations where frontend is on different server than backend
<a name="14.3.0"></a>
## 14.3.0 (2023/04/21)


## Bug Fixes

* firewall no longer fails when MDM or RDM isn't installed
* fixed 'Undefined variable' errors when monitoring isn't installed
* remove obsolete 'warn' arguments
* **healthcheck**
  * readiness endpoint used for checking availability of DPM
  * fixes failures when 'check_availability' is enabled
* **databases:** add missing dbs for databases_cloud playbook

## Features

* **dmm:** one data module for 14.3.x
* add jwt authentication for grpc connection between mmm and one webapp
* **keycloakx:** upgrade to 21.0.1-1
* MDM+RDM example inventory added
* opensearch credentials added to mmm role
* tomcat version bump to 9.0.71
* minio version bump to RELEASE.2023-03-20T20-16-18
* log rotation for postgres implemented
* automate installation of opensearch-plugins behinds proxy
* detect hung connections and reconnect

<a name="14.2.0"></a>
## 14.2.0 (2023/02/16)

## Features

* **nginx:** add fluentbit config for shipping nginx error logs
* **keycloakx:** upgrade to 18.0.2-53

<a name="14.1.0"></a>
## 14.1.0 (2023/01/17)


## Bug Fixes

* **secrets:**
  * update SOPS-encrypted secrets
* **ai:** fix healthcheck endpoints
* **examples:**
  * fix missing secret and password vars
  * align value of the audit crt in nginx_hosts with the rest in example inventories
  * fix minio_ui hostname value in nginx_hosts
  * add opensearch_api_port to RDM standalone inventory
  * add missing Nginx config for MDM standalone
* **logging:**
  * bump opensearch and opensearch dashboards to 2.4.1 for logging
* **dqit:**
  * change AJP port, so it does not collide with Workflow
  * bump tomcat version to 9.0.70
* **mdm-server:** new property server.forward-headers-strategy
* **mdm:** added missing port
* **one_modules:** change parent directory ownership of ONE applications to root
* **orchestration server:** added missing token
* handover document updated
* **firewall:** works even when MDM or RDM is not installed
* lock_version module OS discovery fixes
* **diffie-hellman:** default parameters' size changed to 4096b
* **term-suggestions:**  term-suggestions-api port numbers: changed to the service defaults
* **summary:** fix failing summary when installing plain+mdm standalone

## Features

* removed OneCfg service
* removed AI matching services
* **new services:**
  * Comment
  * Task
  * Workflow
* **DPE:** DPE with JDBC drivers
* **frontend:** add observability tab

<a name="13.9.0"></a>
## 13.9.0 (2022/09/14)

## Features

* new TS APi Service added
* elasticsearch removed in favor of Opensearch
* security of nginx hardened by diffie-hellman
* minio upgrade
* public configuration of IDE
* enabled monitoring for mdm-server
* bump tomcat version to 9.0.65
* bump grafana version to 9.1.5

## Bug Fixes

* **python:** upgrade PIP on RHEL8
* **monitoring:** remove duplicate tasks
* **firewall:** allow outgoing ipv6 connections on loopback interface
* **minio:** wrong command-line parameter in service start

## Refactor

* remove minio as gateway related code
<a name="13.8.1"></a>
# 13.8.1 (2022/07/19)


## Bug Fixes

* **es_backup:** directory ownership fixed
* **grafana:** add prometheus datasource (#3bd54a29)
* **kibana:** configure logs only to stdout in json format
* **dqit:** bump tomcat version to 9.0.64 (#37fc6f38)
* lock fluentd version
* disable dpe debug by default
* **keycloak:**
  * do not restart before systemd unit is available
  * enforce SSL connections
* **mdm_server:** add missing JAVA_OPTS required by default
* **DPE:** DPE's summary added

## Features

* **packaging:** add external roles and collections to the package

<a name="13.8.0"></a>
## 13.8.0 (2022/06/28)

## Bug Fixes

* fixed python2-cryptography on CentOS 7
* fixed ca-certificates package for CentOS 7
* **keycloak:**
  * do not try to restart before systemd unit is available
  * enforce SSL connections
* **mdm_server:** add missing JAVA_OPTS required by default
* **nginx:** increase buffers for /auth to fix MDA
* **DPE:** DPE's been missing summary

## Features

* new content packs management for mmm-backend
* ai-core services refactored
* nlp services removed
* support for AWS RDS Aurora added
* starting, stopping and restarting services using tags enabled
* prometheus datasources added to grafana
* event storage removed
* selfsigned and own-ca certificates possibilities added
* **security:**
  * security hardening for Keycloak realms - secure flag for cookies
  * Keycloak testing users removed by default


<a name="13.7.1"></a>
# 13.7.1 (2022/05/02)

## Bug Fixes

* **exporters:** home directories for prometheus exporters

<a name="13.6.0-3"></a>
# 13.6.0-3 (2022/04/21)

## Bug Fixes

* home directories unified for all services
* **tomcat:** bump tomcat version to 9.0.62

## Features

* SMTP implemented
<a name="13.6.0-2"></a>
# 13.6.0-2 (2022/04/12)

## Bug Fixes

* mmm management port property name fixed
* fixed MDM console login
* fixed cif-bootstrap.jar file searching
* increase mdm-server java memory limits, ensure it's restarted properly
* fixed config permissions
* **hybrid-dpe:**
  * fix example inventory version
  * hybrid-dpe-fix-version
* **standalone:** deleted azure related variables from examples
* fixed config file permissions

## Features

* MDM standalone
* RDM standalone

<a name="13.6.0-1"></a>
# 13.6.0-1 (2022/03/22)

## Bug Fixes

* **AWX:** added apt update for AWX inventory, excluded changes from build (#b12697db)
* set correct permissions for the unpacked DPE filesystem (#3cc16c92)
* **firewall:** implement source filtering for AI services (#955e47ea)

## Features

* added openjdk and adoptionopenjdk support (#d619ed37)
* **nginx:** security (#cd425253)

## Breaking changes

* Several passwords that were hardcoded are now set when creating inventory
  (see the list below). Example were updated to contain the necessary settings.
  All Ansible code was updated accordingly, but in case you are
  using external data or configuration that referece these passwords, you have to
  update them before deploying these data / confiurations.

  * `manta_admin_password`
  * `nginx_default_password`
  * `dqit_admin_password`


<a name="13.6.0"></a>
## 13.6.0 (2022/03/10)

## Bug Fixes

* don't fail when disabling system firewalls (#6f3c6f8d)
* disable Mitogen for Centos7 (#ce0c5894)
* install python-lxml package on CentOS 7 (#5a497b3e)
* fix AI AD missing variable (#546ef372)
* **firewall:** alllow connections from DPE to MDM and RDM internal datasources (#e45fcbf1)
* **aicore:**
  * aicore replaced by multiple roles and one playbook fixed (#92821862)
  * integrate secrets rework into the encrypted file (#33b1cabf)
* **ssl:** connection to postgresql (#4a6c72cc)
* **cs:**
  * adding cors properties (#63354032)
  * env value in init (#23283e1e)
* **database:** connection limit (#62017355)

## Features

* **security:** enable SOPS for Ubuntu reference environment (#051dce88)
* summary generation & collection (#7119d85d)
* added a possibility to replace system repos (#c3f67bd0)
* **firewall:** filter incomming connections by source address (#7306fefa)
* **aicore:** add libgomp package to Debian and RedHat (#2778cc73)
* updated keycloak to 15.1.1 (#d84645b1)
* PGSQL pglocks settings possible to set (#fa8283af)

<a name="13.5.0-1"></a>
# 13.5.0-1 (2022/01/11)


## Bug Fixes

* **security:** increase elastic version to log4shell safe version (#874c55a5)

## Features

* updated version of td-agent

<a name="13.5.0"></a>
## 13.5.0 (2022/01/06)


## Bug Fixes

* **grafana:** security version fix grafana (#84359fc8)
* **process exporter:** version upgrade process exporter (#f916d177)
* **prometheus:** prometheus version upgrade (#cd371981)
* **epel:** nginx repo (#d4d1216)
* **sops:** default secrets in plain text (#a107cee3)
* **frontend:** frontend app-properties updated (#8a3c3b46)
* **secrets:** remove binary tools, download them in package build (#e12eeef3)
* **alertmanager:** version alertmanager (#0fd93d37)
* **keycloak:** java heapsize (#21c72507)
* **node-exporter:** version latest of node exporter (#5482b0d8)
* **mmm:** smtp healt check disabled by default (#febca9aa)
* set aicore package type for CentOS 7 (#9ff78251)

## Features

* **certificates:** added ownca support (#9b1be99b)
* **postgresql:** possibillity to set up ssl mode (#f0de2cab)
* **security:** secrets encryption (#db96b617)
* **nginx:** updated nginx_config role (#4b5d4ccd)
* **documentation:** PDF version of Ansible documentation

<a name="13.4.0-1"></a>
# 13.4.0-1 (2021/12/02)


## Bug Fixes

* **ansible:** manage permissions of /etc/ansible directory (#dd94ee43)
* **bug fixes:** jmespath added to requirements, cert_dir perms fixed (#92d2768a)
<a name="13.4.0"></a>
# 13.4.0 (2021/12/01)


## Bug Fixes

* **aicore:**
  * fixed requirements_installed file creation (#10fb5413)
  * skip platform-dependent pip packages missing (#aea361f8)
  * use full aicore package by default (#742cee47)
* **docs:** add chmod workaround step for prometheus role (#385994cf)
* **ONE-27666:** relaxed binding in security-utils (#dc1b1193)
* **keycloak:** added CentOS 7 support (#050368c4)
* **postgresql:** added CentOS 7 support (#f24b79e6)
* **nginx:**
  * added CentOS 7 support for nginx package (#b4836cff)
  * added CentOS 7 support for python-passlib (#d7098566)
* removed secret vars duplicates (#af7c36ea)
* variable renamed in dqit preflight-check (#2b55b22f)
* **monitoring:**
  * use proper keycloak variable names (#fcc9a82e)
  * added missing rules, fixed naming (#d9b7eb7d)
  * throttle delegated role that competes for APT locks (#50c7793e)
* **node exporter:** updated node exporter version (#53f07efe)

## Features

* update fluentbit to 1.8.10 (#ddce1d60)
* new IDE property in configuration service (#f1f51e61)
* added logs rotation for modules (#97cb23a0)
* added python3 installation for CentOS 7 (#88afa3a8)
* added CentOS 7 support for one_letsencrypt_cert role (#4e3a0431)
* auditor role in Keycloak (#992e105d)
* boolean flag for managing firewall (#07afecfc)
* boolean flag for managing monitoring (#5f6ad5cf)
* **mdm-server:** mdm server in springboot (#3a63692a)
* **java:** added CentOS 7 support for java role (#44604ec9)
* **aicore:** separated variables for full and minimal packages (#53ecb88c)
* **monitoring:** modular monitoring, first working version (#1a3f8f22)

## Refactor

* **rsyslog:** rsyslog tasks included into system role
<a name="13.3.2"></a>
# 13.3.2 (2021/11/12)


## Bug Fixes

* service description (#7e025038)
* add missing firewall rules for orch-console (#d1841da1)
* fix aicore os variables (#1eea2e65)
* firewall playbook renamed for awx run (#003a3d33)
* splitting the set of job in better ratio (AWX well known issue) (#1548f71f)
* remove drivers from hybrid example (#41abc85e)
* pre-commit hook for md-lint is set up to only docs folder (#d2d48cbe)
* move mdm configuration directory (#e8cfc83f)
* disable handling of /var/log/messages using rsyslog
* **firewall:** update package cache before installing firewall packages (#9c964049)
* **az-cli:** pin specific versions (#da51f338)

## Features

* added RedHat support for postgresql_cloud role (#bf000eed)
* **aicore:** added CentOS 7 support (#9b8b20b7)
<a name="13.3.1-1"></a>
# 13.3.1-1 (2021/11/01)


## Bug Fixes

* **fluentbit:** include dropins only when necessary (#2b24d6e2)
* **aicore:** the full aicore package replaced by the minimal (#cfe109dc)

## Features

* add playbook and example inventory for separate hybrid DPE deployment (#f8d539bf)
<a name="13.3.1"></a>
# 13.3.1 (2021/10/25)


## Bug Fixes

* **fluentbit:** fix failed_when condition to work on empty install (#0e8e6277)
* **keycloak:** memory heap (#35b6f885)
* conditions to run db part of playbook only if respective tags are set on the VMs (#8b44e811)
* fix prometheus_exporter role name after renaming (#ceff9e88)
* restore no_log=True in az_login (mistake) (#a5825e86)
* update postgresql jdbc driver to version 42.2.24 (#cfbfa30c)
* sensitive data in one_module is now hidden (#0d83f62d)
* improve error handling in fluentbit handler (#f1a72968)
* wrong variable in mdm_install_dir (#de47c5f1)
* **firewall:**
  * fix nginx rule generation, add missing elasticsearch rule (#769279d7)
  * fix rebase errors, add missing rules (#d69a063c)
  * use correct grafana dashboards commit (#1db2a525)
  * allow waiting for xtables lock (#f8b95f67)
* **logging:** store outputs moved to current matchers (#c2d0e04b)
* **monitoring:**
  * fixed variables and mmm queries (#53a45527)
  * add some missing rules, fix rebase error (#7bea436a)
* **mdm:**
  * fix condition in aip playbook (run mdm frontend when requested) (#338c3bcd)
  * move mdm_frontend to its own group (#56ef440c)

## Features

* **fluentbit:** allow for systemd override, set max_open_files limit to 50000 (#cd0c3bd3)
* **monitoring:**
  * added common role for prometheus exporters (#058dfcab)
  * added nginx monitoring (#a4b9af37)
  * added prometheus alerts dashboard (#23b03555)
* **certificates:** added Centos 8 support (#bb690c1d)
* **firewall:** firewall rules for fluent-bit and monitoring were split (#97a43403)
* monitoring of fluentbit + fluentd (#5bfb168f)
* **logging:** added manta logs and filters (#2f60af16)

## Refactor

* separate role for jmx exporter to unify version and configuration
* implement modular firewall
* fluentbit extracted to separate role + support for conf.d dirs
* **logging:** deleted old fluentd configs, keycloak logs were moved
<a name="13.3.0-1"></a>
# 13.3.0-1 (2021/09/17)


## Bug Fixes

* **componentization:** include mdm on frontend dynamically (#ad6ea5c1)
* **inventories:** add missing parts of nginx config (#04cd2a3b)
* fix hardcoded urls in config-service import (#be46f222)
* internal encryption config improvements (#d1fe4557)
* deleted unused role (#236260e2)
* kibana plugin installation (#66c2ca22)
* remove keycloak.port (#8219275e)
* wrong frontend_token_client (#7499f36a)
* fixed bug with assets folder name (#652e27ea)
* add default passwords (#e07a01dd)
* fix conditionals in properties for components on different hosts (#448bd43f)
* remove condition for triggering manta playbook (#aeac3ac6)
* **postgresql:** fixed pipelining in a task (#f07da05f)
* **package:** fix corrupted files in the package (#4b8cd4f0)

## Features

* added postgres-exporter queries for mmm database (#03ddc9fe)
* updated mmm queries (#ad43add2)
* changed tmp folders for components (#bc83260f)
* **logging:**
  * fluentbit + fluentd setup (#7faa638e)
  * added fluentd and fluent-bit (#8787e87b)
* component versioning (#513a4a33)
* **monitoring:** modular monitoring, the temporary simple version (#2a8e23a7)
* **nginx:**
  * replaced default nginx pages (#cda09c9d)
  * added possibility to choose components (#01bcd736)

## Refactor

* move config from configuration service to module properties
* parts of config depending on groups
* split keycloak clients from hashes for simpler override
* simplify demodata import
* **keycloak:** template the realm file for needed clients only
<a name="13.3.0"></a>
## 13.3.0 (2021/09/03)


## Bug Fixes

* correct submodule settings (#2d02f0e4)
* **vuepress:**
  * vuepress config (#d48ff813)
  * vuepress typo (#b2613e80)

## Features

* support 13.3.0 version, remove older versions (#ce922789)

## Refactor

* remove obsolete variable files from example inventory
<a name="13.3.0-alpha"></a>
# 13.3.0-alpha (2021/09/02)


## Bug Fixes

* **manta:** basename missing for manta_license_key (#4a1fb4d8)
* sync of prometheus scrape config, proper condition for cloud managed db (#3e14649c)
* fixed documentation (#788fd23b)
* renamed ansible config for customers (#b33b0f75)
* RDM's catalog url (#087af4fc)
* add check for defined le_cloud_provider (#b1593dfc)
* calling nginx handler removed (#f3d2c0c4)
* **facts**:
  * facts gathering for ansible_domain (#a1de5d51)
  * dns fact for one_app (#fcee9d97)
* **aicore:**
  * fixed virtualenv re-creation on RedHat Closes ONE-25339 (#489a6cf9)
  * fixed aicore dns resolution (#cff8d686)
  * moved gai.conf file (#d52ba36d)
* **monitoring:** wrong server group in prometheus scrape config for mdm (#4afd1057)

## Features

* added grafana dashboard for keycloak (#4cc25428)
* refactor firewall playbook, add firewall toggle and disable firewall on all production envs (#cba61c5f)
* orchestration server added to hosts (#b143676d)
* added the doc for availability checks in roles (#290f894b)
* Added the ansible.cfg file for customers (#a03ae51c)
* added a documentation for the ansible config (#cebf5b49)
* JMX based monitoring of old Java components (#01ea9c6b)
* cloud db deployment based on set of ONE modules (#3b44add4)
* remade postgresql_exporter role (#864b5660)
* dqit modifications for cloud db; some log cleanup (#0560e569)
* 3rd party versions moved into packages.yml (#e07c1dfe)
* enable heap dumps for ATA JVMs (#8a847f88)
* **keycloak:** Added the enabling of the keycloak metrics-listener event (#6aa8bb98)
* **healthchecks:**
  * added label 'pod' to DPE Prometheus scrape job (#cb1bfcd2)
  * parametrized availability checks in roles (#1e562442)
* **aicore:**
  * rebased with virtualenv (#0bf94474)
  * fixed aicore dns resolution (#c2ff6389)
  * aicore installation via python venv (#84707ecc)
  * added a path for the virtualenv (#7df7119f)
  * splitted aicore systemd unit (#7e1d74af)
* **onecfg:** support known properties for configuration service (#95c76b0d)
* **manta:** support for optional deployment (#97a9f9e6)
* **dpe:** support provisioning of dpe drivers (#8ff0d895)

## Refactor

* new groups for dqit components
* remove internal MANTA license from the build
* **vars:** configure specific license for each component

<a name="13.2.1"></a>
# 13.2.1 (2021/08/18)


## Bug Fixes

* extending the license location (#a73ae06c)
* added lookups_import boolean (#1a3a157d)
* orchestration nginx config + keycloak url (#24f578cd)
* add java to orchestration server (#c249ff1e)
* remove services_online from templates (#c1ced589)
* missing quotes (#4f013b93)
* fixing keycloak installation (#d2aef9db)
* fixing ONE-23507 (#8c2aba05)
* fixing keycloak installation (#10070eeb)
* after merge (#ac225544)
* rhel hosts update (#21a9ee53)
* qa- inventories update (#de0e44ca)
* resolving of grafana_datasource module within external grafana role (#6105b245)
* qa-inventories update (#a479ff16)
* enable firewall on orchestration server (#5ae5296e)
* (IDP-309) additional variables for azure-production envs (#ab031ff5)
* azure collection added into list (#ef0cbb52)
* set KillMode=control-group for keycloak (to fix issues) and minio (just to be sure) (#f6788f67)
* downgrade of azure.azcollecton (#caabded6)
* (ONE-24929) Added the installing of pg_stat_statements and fixed exporter queries (#592883c3)
* fixing lint errors (#9058c01e)
* (ONE-24982) Fixed RedHat packages installation (#49e1efd3)
* (ONE-24929) Using pg_stat_user_tables instead of of pg_stat_statements (#0f11ccb1)
* (ONE-24981) mitogen is temporarily disabled (#89573cd6)
* (ONE-24802) set basic_auth to true by default (#c1c34839)
* (ONE-24802) set basic_auth to true by default (#85a1b681)
* (ONE-25053) - proper domain variable & dpm public key (#d2547952)
* (ONE-25007) license fix (#ac5c3d97)
* **minio:** minio monitoring improvements (#0f496571)
* **manta:**
  * monitoring breaks Manta server on startup (#7a46345a)
  * monitoring Manta service utility, alerts and dashboards for Manta (#fb46ca4e)
* **alerts:** blackbox exporter alerts expressions as raw code (#1b5c9f20)
* **one-24580:** app user as db owner (#3bebdb03)
* **vars:** mmm_install_dir variable references old name (#5d8a116a)
* **mdm:** fix default application.properties for mdm (#807357da)
* **users:**
  * switch users to system accounts (#e2b81731)
  * switch users to system accounts (#3f461a7b)
* **dns_suffix:** fix hardcoded values and doc (#8832bc00)
* **keycloak:**
  * fix JBOSS_PIDFILE env variable (#e57451d7)
  * install to version directory (#a45c6eb1)
  * bump monitoring spi to 2.4.0 (#5653fa59)
* **nginx:**
  * remove plain HTTP listeners (#4400cb76)
  * reload nginx on cert chagne (#e5c00871)
* **elasticsearch_exporter:** add dedicated elastic search_exporter user and group (#c17b9e00)

## Features

* add system role for managing system users and groups (#402ced31)
* parametrize Java role to select versions installed and default version (#7476217c)
* bump tomcat version (#2b7210a2)
* rhel-download packages from s3 (#a6f7c8fd)
* (IDP-309) requirements split to support Ansible Galaxy within AWX (#35e4d72f)
* (PDI-36) Fixed flaws from customer AWS installation (#3a862de1)
* (ONE-21996) Actuator endpoints are disabled (#657ec642)
* add Zdenek Belehradek's dev inventory (#6407ac40)
* (IDP-309) modifications for externalized Let's Encrypt & DNS CNAMEs roles (#79031389)
* added .pre-commit-config.yaml and .editorconfig files (#e4ece0f9)
* one-23232 Added prometheus alerts for elastic search (#7fa6e9e9)
* (ONE-24802) Added kibana basic auth (#684822aa)
* (ONE-24802) Added a possibility to set up basic auth credentials (#339e7775)
* (ONE-24802) added RedHat support (#e6a28a13)
* (ONE-24802) Added kibana basic auth (#213435d5)
* (ONE-24802) Added a possibility to set up basic auth credentials (#4e4be10e)
* (ONE-24802) added RedHat support (#21bbaf72)
* **inventory:**
  * development inventory for Anton (#1867e4ae)
  * updated Anton Alekseev's dev inventory (#7b4a44bd)
* **onecfg,vars:** add support for config via application properties in one module role (#9f40ba4e)

## Refactor

* external-like roles moved into this repository
* **vars:** organized files and removed unused variable
## Unreleased
### Added
- Role to manage user accounts
- all servers are now firewalled

## [0.2.0] - 2021-15-07
### Added
- New ansible roles for AIP modules:
    - installation of RDM webapp and server. (ONE-18882)
    - installation of MDM webapp and server. (ONE-19224)
    - installation of DQIT webapp, DQIT server and Tomcat. (ONE-19084)

- New groups for hosts for AIP modules introduced and playbook for AIP deployment created.
- Inventory for penetration testing environment in Karlin.
- Linting pipeline added.
- Allow for different download types for ONE modules. (ONE-20516)
- Allow multiple system services in ONE module.
- Configuration for deployment of orchestration server - playbook + vars

### Changed
- Roles for logging stack (Elasticsearch, Kibana) replaced by a wrapper of the community role from Galaxy (ONE-18571)
- Roles for monitoring stack (Prometheus, Grafana, PostgreSQL exporter) replaced by a wrapper of the community role from Galaxy (ONE-18572)
- Role for PostgreSQL replaced by a wrapper of the community role from Galaxy (ONE-18573)
- Upgraded Postgres major version to 13
- The whole deployment is now run from site.yml from root.
- Unified the variables for ONE modules.
- BREAKING CHANGE: Removed `group_vars` directory and replaced with defaults and symlinks to allow for multiple inventories support.
- New variables for configuration service initial data load introduced.
- BREAKING CHANGE: ingress role renamed to nginx, it's vars prefixed to `nginx_*`. `default_ingress_hosts` variable renamed to `nginx_hosts`.
- refactor: `letsencrypt` role merged into `certificates` role - now handles `selfsigned`, `acme` and `provided` certificates, variable `certificates` for configuration.

### Fixed
- Wrong system user running ONE services (frontend, dpm, dpe).

## [0.1.0] - 2020-10-07
### Added
- Own Ansible roles for dependencies, ONE modules, logging and monitoring stack
- Ubuntu / Centos support (with some known issues and limitations)
- Inventories for reference deployment in Karlin
