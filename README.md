# Composite Container-based Application Specification

## Problem Statement
Currently there is no standard mechanism to define a composite multi-container application or composite service composed of aggregate pre-defined building blocks spanning multiple hosts and clustered deployments. In addition, the associated metadata and artifact management requires separate processes outside the context of the application itself. 

## What is Nulecule?
It's a made-up word meaning ["the mother of all atomic particles"](http://simpsons.wikia.com/wiki/Made-up_words) pronounced `NOO-le-kyul`, like "molecule".

Nulecule defines a pattern and model for packaging complex multi-container applications, referencing all their dependencies, including orchestration metadata in a container image for building, deploying, monitoring, and active management.

Nulecule specification enables complex applications to be defined, packaged and distributed using standard container technologies. The resulting container includes dependencies while supporting multiple orchestration providers and ability to specify resource requirements. The Nulecule specification also supports aggregation of multiple composite applications. The Nulecule specification is container and orchestration agnostic, enabling the use of any container and orchestration engine.

## Nulecule Specification Highlights

* Application description and context maintained within a single container through extensible metadata
* Composable definition of complex applications through inheritance and composition of containers into a single, standards-based, portable description.
* Simplified dependency management for the most complex applications through a directed graph to reflect relationships.
* Container and orchestration engine agnostic, enabling the use of any container technology and/or orchestration technology

## “The Big Picture”

![Alt Nulecule specification high-level story.](/images/NuleculeHigh-LevelStory.png "Nulecule specification high-level story")

## Glossary
* __Container Image__ - Platform-agnostic term referring to Docker, Rkt or other packaging and transport protocol
* __Layered Image__ - The foundation image of a container plus other tools, applications and content added
* __Association__ of container images to the multi-container Nulecule application:
  + __Aggregation__ of one or more discrete container images integral to the operation and coupled to the lifecycle of the Nulecule application - can be another Nulecule Application or container image reference
  + __Composition__ refers to one or more container images that are required and tightly coupled to the Nulecule application - can be another Nulecule Application or container image reference
* __Include__ - Refers to the ability to include common resources, parameters or definitions needed to deploy onto a orchestration provider. For example, an OpenShift provider may include the kubernetes provider artifacts and add OpenShift functionality on top of kubernetes capabilities.
* __Provider__ - Plugin interface for specific deployment platform, an orchestration provider
* __Dependency Management__ - Refers to the ability to define order of deployment and managed dependencies including configurable parameters layered on top of stock container images, as well as the providers included in the application definition
* __Directed Graph__ - Declarative representation of dependencies in the context of a multi-container Nulecule application
* __Parameters__ - Variables that can have default values and can be overridden by answerfile.conf

## Deployment User Experience

Here's an example using the [atomicapp reference implementation](https://github.com/projectatomic/atomicapp) with a kubernetes provider.

### Option 1: interactive

Run the image. You will be prompted to override defaults
```
[sudo] atomic run projectatomic/helloapache
```

## Option 2: unattended

1. Create file `answers.conf` with these contents:

        [general]
        provider = kubernetes

        [helloapache-app]
        image = centos/httpd # optional: choose a different image
        hostport = 80        # optional: choose a different port to expose

1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/helloapache
        ...
        helloapache

### Option 3: install and run

You may want to download the application, review, edit the answerfile then run.

1. Download the application files using `atomic install`

        [sudo] atomic install projectatomic/helloapache

1. Rename `answers.conf.sample`

        mv answers.conf.sample answers.conf

1. Edit `answers.conf`, review files if desired and run

        $ [sudo] atomic run projectatomic/helloapache
        ...
        helloapache

## Developer User Experience


1. Develop an architecture to define how the services are connected and exposed.
1. Create Dockerfiles and artifacts to package services as container images.
1. Create provider files, e.g. for kubernetes pod, service, replication controller files
1. Reviews example templates of the container application specification
1. Builds the deployment container describing the application.
1. Pushes all container images to a registy.

## Implementations

This is only a specification. Implementations may be written in any language. See [implementation guide](/docs/implementation_guide.md) for more details.

### Developer tooling

Developer implementation provides tooling to help developers quickly package several containers as a unit. It may be as simple as generating a template to start from or as complex as a GUI to develop and provide graphical representation of the target deployment.

### Deployment tooling

Deployment implementation provides tooling for deploying the complete application using this spec.

* Reference implementation (python): https://github.com/projectatomic/atomicapp

### Contributing

Please review the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## TODO

* Create schema validation script

