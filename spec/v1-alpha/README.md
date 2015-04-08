# Application Template

**NOTE**: This is a proof-of-concept effort that is expected to change dramatically.

## template.yaml

The yaml file is the primary file defining the application and relationship to dependencies. See [OpenShift documentation](http://docs.openshift.org/latest/using_openshift/templates.html).

## Directory Layout

```
├── template.yaml
├── Dockerfile
├── <provider_files_dir>
│   ├── ...
│   └── <provider_files>
└── README.md
```

* `template.yaml`: application template
* `Dockerfile`: standard packaging for this application metadata
* `<provider_files_dir>`: directories of provider-specific files referenced in manifest
  * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider, e.g. kubernetes pod and service files.
* `README.md`: information for deploying this application targetted towards deployment ops sysadmin


## README.md

The README.md is the human-readable document for the sysadmin. It describes the application in enough detail so an operator can make parameterization and other deployment decisions.

NOTE: This is optional. It is possible for some applications to be "self-describing" through well-written descriptions and input validation.
