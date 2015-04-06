# Application specification

**NOTE**: This is a proof-of-concept effort that is expected to change dramatically.

## app.yaml

The yaml file is the primary file defining the application and relationship to dependencies. It is largely based on [OpenStack Heat](http://docs.openstack.org/developer/heat/template_guide/hot_guide.html) and [AWS CloudFormation](http://aws.amazon.com/cloudformation/aws-cloudformation-templates/) orchestration templates.

Heat provides some standard ways of defining metadata:

* a parameterization standard, including input validation
* a way to nest or inherit from other application metadata
* a plugin or provider model via resource `type`
* a simple model for describing many resources and associated files
* support for local or remote sources

The yaml file defines applications in 3 ways:

* **local**: an application whose provider files and metadata are contained in the local context. See the ["wordpress" example](/spec/v1-alpha/examples/myapp-heat/app.yaml).
* **composite**: an application which has both local and remote sources. See the ["mariadb" example](/spec/v1-alpha/examples/myapp-heat/app.yaml).
* **extended**: an application which inherits metadata from a local or remote source container but overrides parameters. Use `"kubernetes::metadata": docker://remote/app-image"` instead of `"type": "kubernetes::metadata"`. See the ["myapp" example](/spec/v1-alpha/examples/myapp-heat/app.yaml).

There are three main sections in the yaml file: parameters, resources and outputs.
* `parameters`: a section defining parameters for this application.
  * `description`: string
  * `defaults`: parameter defaults
* `resources`:
  * elements:
    * `type`: specifies provider, e.g. "kubernetes::metadata"
    * `derived_from`: a nested local or remote application. Remote apps should prepend the protocol, ex. `docker://`
    * `deploy`: a list of provider files to deploy
    * `depends_on`: specifies a dependent resource. The service listed will be created first.
    * `properties`: application parameters. May be "hard-coded" or reference another part of the file such as the `parameters` section.
* `outputs`: human- or machine-readble output. NOTE: it's not clear how this will be used.

## Directory Layout

```
├── app.yaml
├── Dockerfile
├── <provider_files_dir>
│   ├── ...
│   └── <provider_files>
└── README.md
```

* `app.yaml`: application manifest
* `Dockerfile`: standard packaging for this application metadata
* `<artifacts>`: directories of provider-specific files referenced in manifest
  * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider, e.g. kubernetes pod and service files.
* `README.md`: information for deploying this application targetted towards deployment ops sysadmin


## README.md

The README.md is the human-readable document for the sysadmin. It describes the application in enough detail so an operator can make parameterization and other deployment decisions.

NOTE: This is optional. It is possible for some applications to be "self-describing" through well-written descriptions and input validation.
