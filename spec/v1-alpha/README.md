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


## Directory Layout

* `Dockerfile`: standard packaging for this application metadata
* `Atomicfile`: application manifest
* `graph`: directories of applications referenced in Atomicfile
  * contains kubernetes files
  * optional params.conf file for app-specific params
* `params.conf`: runtime parameters for application


```
├── Dockerfile
├── Atomicfile
├── init
│   └── myapp
│       └── run.sh
├── graph
│   └── myapp
│       ├── pod.json
│       ├── replication_controller.json
│       ├── service.json
│       └── params.conf
└── params.conf

```
