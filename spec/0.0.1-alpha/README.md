# Container Application Specification

**NOTE**: This is a proof-of-concept effort that is expected to change dramatically.

#### Version 0.0.1-alpha

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The Container Application Specification is licensed under [GNU Free Documentation License Version 1.3, 3 November 2008](https://www.gnu.org/copyleft/fdl.html).

## Introduction

The Container Application specification is a project to describe 'an Application' that is composed of a set of dependend Container Applications (containerapp). The Container Application specification defines a set of files required to describe such an containerapp. These files can then be used by other tools to deploy containerapp. Developers may use a tool set to generate most of the containerapp files. Additional utilities can also take advantage of the resulting files, such as testing tools.

### Versioning

Within this specification we follow [the semantic versioning pattern](http://semver.org/spec/v2.0.0.html). 

## Revision History

Version | Date | Notes
--- | --- | ---
0.0.1-alpha | 2015-mm-dd | TBD
v1-alpha | 2015-04-10 | reversioned to 0.0.1-alpha


## Specification

### Format

The files describing a containerapp in accordance with the Container Application Specification are represented using [YAML 1.2](http://www.yaml.org/spec/1.2/spec.html) or [JSON](http://json.org/).

All field names in the specification are **case sensitive**.

By convention, the containerapp specification file is named `Atomicfile`. The Atomicfile is the primary file defining the containerapp and it's relationship to dependencies.

### Data Types

Primitive data types in the Container Application Specification are based on the types supported by the [JSON-Schema Draft 4](http://json-schema.org/latest/json-schema-core.html#anchor8).

The formats defined by the Container Application Specification are:

Common Name | [`type`](#dataTypeType) | [`format`](#dataTypeFormat) | Comments
----------- | ------ | -------- | --------
integer | `integer` | `int32` | signed 64 bits
float | `number` | `float` | 
string | `string` | |
byte | `string` | `byte` |
boolean | `boolean` | |
date | `string` | `date` | As defined by `full-date` - [RFC3339](http://xml2rfc.ietf.org/public/rfc/html/rfc3339.html#anchor14)
dateTime | `string` | `date-time` | As defined by `date-time` - [RFC3339](http://xml2rfc.ietf.org/public/rfc/html/rfc3339.html#anchor14)
password | `string` | `password` | Used to hint UIs the input needs to be obscured.

### Schema

#### <a name="containerAppObject"></a>Container Application Object

This is the root object for the specification.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="containerAppName"></a>name | `string` | **Required.** The human readable name of the Container Application.
<a name="containerAppDescription"></a>description | `string` | **Required.** The human readable description of the Container Application.
<a name="containerAppVersion"></a>appversion | `string` | **Required.**  The semantic version string of the Container Application.
<a name="containerAppSpecVersion"></a>specversion | `string` | **Required.** The semantic version string of the Container Application Specification used to describe the app. The value MUST be `"0.0.1-alpha"`. 
<a name="containerAppGraph"></a>graph | [ [GraphObject](#graphObject) ] | **Required.** A list of depending containerapps. Strings may either match a local graph sub directory or an another containerapp-spec compliant container image that can be pulled via a provider.
<a name="containerAppRequirements"></a>requirements | [ [RequirementsObject](#requirementsObject) ] | A list of requirements of this containerapp.
<a name="containerAppParameters"></a>params | [ [ParametersObject](#parametersObject) ] | A list of parameters the containerapp requires, has set defaults or needs user input.
<a name="containerAppLicenseObject"></a>license | [License Object](#licenseObject) | The license information for the containerapp.

#### <a name="graphObject"></a>Graph Object

The graph is a list of items (containerapps) the Container Application depends on.

##### Fields of a Graph Item Object

Field Name | Type | Description
---|:---:|---
<a name="dependingContainerAppName"></a>name | `string` | **Required.** The name of a containerapp the Container Application depends on.
<a name="dependingContainerAppRepository"></a>repository | `string` | The name of the repository where the a containerapp could be found.

##### Graph Item Object Example:

```yaml
---
  name: "atomicapp-mongodb"
  repository: "registry.company.example.com"
```

```js
{
  "name": "atomicapp-mongodb",
  "repository": "registry.company.example.com"
}
```

#### <a name="requirementsObject"></a>Requirements Object

The list of requirements of the Container Application. It MAY be [Storage Requirement Objects](#storageRequirementsObject) (for a persistant Volume).


#### <a name="storageRequirementsObject"></a>Storage Requirements Object

This describes a requirement for persistent, read-only or read-write storage that should be available to the containerapp on runtime. The name of this object MUST be `"persistantVolume"`.

##### Fields of Storage Requirement

Field Name | Type | Description
---|:---:|---
<a name="containerAppRequirementsName"></a>name | `string` | **Required.** A name associated with the storage requirement.
<a name="containerAppRequirementsAccessMode"></a>accessModes | `string` | **Required.** May be `"ReadWrite"` or `"ReadOnly"`.
<a name="containerAppRequirementsSize"></a>size | `integer` | **Required.** Size of required the storage.

##### Storage Requirement Example:

```yaml
---
- persistantVolume:
    name: "var-lib-mongodb-data"
    accessMode: "ReadWrite"
    size: 4 # GB by default
```
```js
  {
    "persistantVolume": {
      "name": "var-lib-mongodb-data",
      "accessMode": "ReadWrite",
      "size": 4
    }
  }
```


#### <a name="parametersObject"></a>Parameters Object

Parameters the containerapp requires, has set some defaults for or needs user input.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="parametersDescription"></a>description | `string` | **Required.** A human readable description of the parameter.
<a name="parametersConstraints"></a>constraints | [ConstraintObject](#constraintObject) | An optional definition of constraints to the parameter.
<a name="parametersDefault"></a>default | `string` | An optional default value for the parameter.

##### Parameters Object Example:

```yaml
description: mongoDB Admin password
constraints: 
  - allowed_pattern: "[A-Z0-9]+"
    description: Must consist of characters and numbers only.
```
```js
{
  "description": "mongoDB Admin password",
  "constraints": [
    {
      "allowed_pattern": "[A-Z0-9]+",
      "description": "Must consist of characters and numbers only."
    }
  ]
}
```

#### <a name="constraintObject"></a>Constraint Object

Constraints to the parameter.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="constraintObjectPattern"></a>allowed_pattern | `string` | **Required.** A human readable description of the parameter.
<a name="constraintObjectDescription"></a>description | `string` | **Required.** A human readable description of the parameter.


#### <a name="licenseObject"></a>License Object

License information for the Container Application.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="licenseName"></a>name | `string` | **Required.** The license name used for the API.
<a name="licenseUrl"></a>url | `string` | A URL to the license used for the API. MUST be in the format of a URL.

##### License Object Example:


```yaml
name: Apache 2.0
url: http://www.apache.org/licenses/LICENSE-2.0.html
```
```js
{
  "name": "GNU GPL, Version 3",
  "url": "https://www.gnu.org/copyleft/gpl.html"
}
```


## Directory Layout

```
├── Atomicfile
├── Dockerfile
├── <provider_files_dir>
│   ├── ...
│   └── <provider_files>
└── README.md
```

* `Atomicfile`: Container Application definition
* `Dockerfile`: standard packaging for this containerapp
* `<provider_files_dir>`: directories of provider-specific files referenced in containerapp definition file
  * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider
* `README.md`: information for deploying this application


## README.md

The README.md is the human-readable document. It describes the containerapp in enough detail so an operator can make parameterization and other deployment decisions.

NOTE: This is optional. It is possible for some applications to be "self-describing" through well-written descriptions and input validation.
