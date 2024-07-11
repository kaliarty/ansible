# Ansible reference deployment
This repository (package) contains the Ansible codebase for reference deployment of Ataccama ONE 2.0 and Ataccama AIP software.

Ansible is an open-source software provisioning, configuration management, and application-deployment tool enabling infrastructure as code. See the respective part of the docs on how to install it before usage.

## Documentation
Documentation is in the [docs](docs/) directory, which is part of this package. Internally (Ataccama only) - this documentation is available at https://engineering.pages.ataccama.dev/src/one/ops/ansible/.

Rendering: install mkdocs using pip, install weasyprint using package manager, run mkdocs. Issue: Debian Buster: https://github.com/Kozea/WeasyPrint/issues/1411

### Installation & requirements

To prepare a working Ansible setup, please follow the [requirements section](docs/installing_ansible.md) in our documentation.

### Project structure

The structure of the repository (package) is as follows:
- `./ansible/defaults/` (repo only) - global default variable files that are used to describe and configure the deployment. These ARE overridable.
- `./ansible/collections/` - place for Ansible collections. List with third-party collections and versions is specified in `./ansible/collections/requirements.yml` file.
- `./ansible/files/` - global files that are necessary for the deployment.
- `./ansible/inventories/` - inventory files and variables with regularly managed servers. Note, that variables here are overridden from global `./ansible/group_vars`.
- `./ansible/roles/` - place for Ansible roles for all needed components. List with third-party roles and versions is specified in `./ansible/roles/requirements.yml` file.
- `./ansible/templates/` - place for global template files used.
- `./ansible/group_vars/` - place for global variables files.
- `./docs/` - documentation of this project.

#### Package versions
We keep the versions of the ONE packages in `packages.yml` file (see `./defaults/` directory for reference).
Apart from the version, you can configure for each module `package_download type`:
- `maven_artifact` (default) - uses packages in Artifactory defined in `artifactory_repo_url`,
- `remote_url` - uses remote location to download package, define `package_url` to specify url to the package,
- `local` - uses package downloaded to your local machine, specify `package_location` to specify path.

Other options may be supported in the future eventually.

### Deployment of the platform
#### Installing requirements
Before running any playbook, you need to install dependency collection and roles from Ansible Galaxy defined in `requirements.yml` file. Use

```shell
ansible-galaxy install -r collections/requirements.yml
ansible-galaxy install -r roles/requirements.yml
```
command, check the file for reference.

#### Playbooks
Playbooks to deploy separate components are places in the root directory. To deploy the whole application stack at once, run the following command from the root dir:

```shell
ansible-playbook -u <your-username> -i <path-to-hosts-file> site.yml -b
```
To install only a part of ONE 2.0 run a different playbook from the directory, or uncomment unnecessary components in `site.yml`

With the various setup in your inventory `hosts` file, you can set up many types of deployment.
