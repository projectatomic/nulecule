# Implementation Guide

This specification has been fully described in the [schema.json](/spec/0.0.2/schema.json) file. Developer and deployment tools should be implemented using this file.

## Developer Tools

Developer tooling helps application developers or designers get going quickly. Tools may be template-based or wizard-style tools, command line or graphical interface. When creating a tool for developers decide how much assistance you want to expose for the providers. Each provider has its own documentation and potential tooling but integrating provider features can be a big help to getting something working quickly.

Wizard-style tools that generate the files for an application require these fields for input:

* name
* description
* version (application)

Each "application" component the user wants to define will compose the "graph" for the Nulecule. A component may either be a remote application or defined locally in the directory structure.

**Remote applications**

Remote applications are simply container images, for example `someuser/mariadb-app`. No other information is needed.

**Local applications**

Local applications are defined by a directory in the graph. These fields are required for input:

* application name: this is added to the Nulecule graph and creates a directory in the graph.
* provider: a subdirectory of the application directory

**Providers**

Provider files may be generated based on some templates. Providing a mechanism to parameterize these files helps the developer understand how parameterization works. For example, if a set of kubernetes template files are pulled in allowing the developer to parameterize some values in the pod file would update the pod file and create a `key = value` pair in the application section of the `params.conf` file. For required values without defaults set the value to `None` in `params.conf`. With this example as a starting point the developer can then easily manipulate parameters by manually editing the files based on the demonstrated pattern.

## Runtime Tools

Reference implementation (python): https://github.com/projectatomic/atomicapp
