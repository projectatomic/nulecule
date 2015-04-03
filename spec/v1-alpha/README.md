# Application specification

**NOTE**: This is a proof-of-concept effort that is expected to change dramatically.

## app.yaml

The yaml file is the primary file defining the application and relationship to dependencies. It is based on the [TOSCA specification](http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/TOSCA-Simple-Profile-YAML-v1.0.pdf). This implementation utilizes a small fraction of the TOSCA specification. Users of [Heat](https://wiki.openstack.org/wiki/Heat) and [AWS CloudFormation](http://aws.amazon.com/cloudformation/aws-cloudformation-templates/) orchestration templates will find syntax familiar.

The yaml file defines applications in 3 ways:

* **local**: an application whose provider files and metadata are contained in the local context. See the ["wordpress" example](/spec/v1-alpha/examples/myapp-tosca/app.yaml).
* **composite**: an application which has both local and remote sources. See the ["mariadb" example](/spec/v1-alpha/examples/myapp-tosca/app.yaml).
* **extended**: an application which inherits metadata from a local or remote source container but defines its own image and other parameters. It uses the "derived_from" key and has overriding parameters. See the ["myapp" example](/spec/v1-alpha/examples/myapp-tosca/app.yaml).

There are three main sections in the yaml file: inputs, node_templates and outputs.
* `inputs`: a section defining parameters for this application.
  * `description`: string
  * `defaults`: parameter defaults
* `node_templates`:
  * sub-section for each application service
  * components:
    * `derived_from`: a node_template or remote application
    * `artifacts`: a list of provider artifacts
    * `requirements`: specifies a dependent service. The service listed will be started first.
    * `properties`: application parameters. May be "hard-coded" or reference another part of the file such as the `inputs` section.
* `outputs`: human- or machine-readble output.

NOTE: The `interfaces.lifecycle` use is unclear at this time. Ideally this is either hidden or abstracted so the application developer can define simple lifecycle commands.

## Directory Layout

```
├── app.yaml
├── Dockerfile
├── <artifacts_dir>
│   ├── ...
│   └── <provider_files>
└── README.md
```

* `app.py`: application manifest
* `Dockerfile`: standard packaging for this application metadata
* `<artifacts>`: directories of provider-specific files referenced in manifest
  * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider, e.g. kubernetes pod and service files.
* `README.md`: information for deploying this application targetted towards deployment ops sysadmin


## README.md

The README.md is the human-readable document for the sysadmin. It describes the application in enough detail so an operator can make parameterization and other deployment decisions.

