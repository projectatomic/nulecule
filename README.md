# Container Application Specification

## Goals

1. Provide a simple, flexible way to describe a multi-container application, including all dependencies.
1. Provide a way for an application designer to describe an application while allowing a sysadmin a clear way to parameterize the deployment at runtime.
1. Provide a versioned specification for developer tools and runtime implementations to agree on.

## User Experience

### Kelly the System Administrator

Kelly is deploying an application that she's been provided by Acme Corp's internal developer team, led by Rufus.

1. Download the application README and answerfile template

         atomic run <application-container-image> --dry-run

2. Review README and edit the local answerfile for your deployment environment
3. Deploy the application

         atomic run <application--container-image> --answerfile answerfile.conf

At deployment the `<application--container-image>` is pulled, the target deployment files (e.g. kubernetes) are parameterized using the `answerfile.conf` and the application is started.

### Rufus the Developer
TBD

## Implementations

This is only a specification. Implementations may be written in any language.

### Developer tooling

Developer implementation provides tooling to help developers quickly package several containers as a unit. It may be as simple as generating a template to start from or as complex as a GUI to develop and provide graphical representation of the target deployment.

### Deployment tooling

Deployment implementation provides tooling for deploying the complete application using this spec.

* Python implementation: https://github.com/vpavlin/atomicapp-run

## TODO

* Create machine-readable schema that is self-documenting
* Create schema validation script

