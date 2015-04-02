# THIS IS WRONG -- TBD

## Atomicfile

```
{
  "name": String,
  "description": String,
  "appversion": String,
  "graph": [ String, ...]
  "specversion": String,
}
```

* `name`: arbitrary name
* `description`: arbitrary description
* `appversion`: version of the application
* `graph`: list of applications. Strings may either match a local graph sub directory or an application metadata container that can be pulled via docker.
* `specversion`: version of this specification, ex. "v1-alpha"

## Directory Layout

```
├── Atomicfile
├── Dockerfile
├── graph
│   └── <application>
│       └── <provider>
│           ├── <PROVIDER_FILES>
│           └── params.conf
├── params.conf
└── README.md

```

* `Atomicfile`: application manifest
* `Dockerfile`: standard packaging for this application metadata
* `graph`: directories of applications referenced in Atomicfile separated by provisioning provider
  * `<application>`: a directory whose name matches the graph list in the Atomicfile.
  * `<provider>`: a directory whose name matches a list (TBD) of container or orchestration technologies: `kubernetes`, `docker`, `compose`, `systemd`, etc.
      * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider, e.g. kubernetes pod and service files.
      * `params.conf`: optional file for app-specific params
* `params.conf`: runtime parameters for application
* `README.md`: information for deploying this application targetted towards deployment ops sysadmin


## params.conf

App-specific section overrides global.

```
[global]
foo = bar

[app1]
boo = baz

[app2]
foo = buzz
```

## README.md

The README.md is the human-readable document for the sysadmin. It describes the application in enough detail so an operator can make parameterization and other deployment decisions.

