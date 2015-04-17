# Container Application Specification

## Goals

1. Provide a simple, flexible way to describe a multi-container application, including all dependencies.
1. Provide a way for an application designer to describe an application while allowing a sysadmin a clear way to parameterize the deployment at runtime.
1. Provide a versioned specification for developer tools and runtime implementations to agree on.

## User Experience

### Kelly the System Administrator

Kelly is deploying an application that she's been provided by Acme Corp's internal developer team, led by Rufus.

1. Download the application README and answerfile template

         atomic run <deployment-container-image> --dry-run

2. Review README and edit the local answerfile for your deployment environment
3. Deploy the application

         atomic run <deployment-container-image> --answerfile answerfile.conf

At deployment the `<deployment-container-image>` is pulled, the target deployment files (e.g. kubernetes) are parameterized using the `answerfile.conf` and the application is started.

### Rufus the Developer

Rufus has been tasked to package an existing application into container images that can be deployed via kubernetes. He has some combination of RPMs, jar files and source code.

1. Develop an architecture to define how the services are connected and exposed.
1. Create Dockerfiles and artifacts to package services as container images.
1. Create provider files, e.g. for kubernetes pod, service, replication controller files
1. Reviews example templates of the container application specification
1. Builds the deployment container describing the application.
1. Pushes all container images to a registy.

## Implementations

This is only a specification. Implementations may be written in any language. See [implementation guide](/implementation_guide.md) for more details.

### Developer tooling

Developer implementation provides tooling to help developers quickly package several containers as a unit. It may be as simple as generating a template to start from or as complex as a GUI to develop and provide graphical representation of the target deployment.

### Deployment tooling

Deployment implementation provides tooling for deploying the complete application using this spec.

* Reference implementation (python): https://github.com/vpavlin/atomicapp-run

### Contributing

Please review the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## TODO

* Create schema validation script

