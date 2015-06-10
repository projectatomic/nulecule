# Composite Container-based Application Specification

`/NOO-le-kyul/` (n.) a made-up word meaning ["the mother of all atomic particles"](http://simpsons.wikia.com/wiki/Made-up_words). Sounds like "molecule". But different.

**Package once. Run anywhere.** With pluggable orchestration providers you can package your application to run on OpenShift, Kubernetes, Docker Compose, Helios, Panamax, Docker Machine, etc. and allow the user to choose the target when deployed.

**Compose applications from a catalog.** No need to re-package common services. Create composit applications by referencing other Nulecule-compliant apps. Adding a well-designed, orchestrated databse is simply a reference to another container image.

**MSI Installer for containers.** Replace your shell script and deployment instructions with some metadata.

**Change runtime parameters for different environments.** No need to edit files before deployment. Users can choose interactive or unattented deployment. Guide web interface users with parameter metadata to validate user input and provide descriptive help.

## Problem Statement
Currently there is no standard mechanism to define a composite multi-container application or composite service composed of aggregate pre-defined building blocks spanning multiple hosts and clustered deployments. In addition, the associated metadata and artifact management requires separate processes outside the context of the application itself. 

## What is Nulecule?

Nulecule defines a pattern and model for packaging complex multi-container applications, referencing all their dependencies, including orchestration metadata in a container image for building, deploying, monitoring, and active management.

Nulecule specification enables complex applications to be defined, packaged and distributed using standard container technologies. The resulting container includes dependencies while supporting multiple orchestration providers and ability to specify resource requirements. The Nulecule specification also supports aggregation of multiple composite applications. The Nulecule specification is container and orchestration agnostic, enabling the use of any container and orchestration engine.

**[Glossary of terms](docs/glossary.md)**

## Nulecule Specification Highlights

* Application description and context maintained within a single container through extensible metadata
* Composable definition of complex applications through inheritance and composition of containers into a single, standards-based, portable description.
* Simplified dependency management for the most complex applications through a directed graph to reflect relationships.
* Container and orchestration engine agnostic, enabling the use of any container technology and/or orchestration technology

## “The Big Picture”

![Alt Nulecule specification high-level story.](/images/NuleculeHigh-LevelStory.png "Nulecule specification high-level story")

## Deployment User Experience

Here's an example using the [atomicapp reference implementation](https://github.com/projectatomic/atomicapp) with a kubernetes provider.

### Option 1: interactive

Run the image. You will be prompted to provide required values that are missing from the default configuration.
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

See the [Getting Started with Nulecule guide](docs/getting-started.md).

## Implementations

This is only a specification. Implementations may be written in any language. See [implementation guide](/docs/implementation_guide.md) for more details.

**Reference implementation** https://github.com/projectatomic/atomicapp

### Developer tooling

Developer tooling is TBD. There is some work planned for [DevAssistant](http://devassistant.org/).

### Contributing

Please review the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

###Communication channels

* IRC: #nulecule (On Freenode)
* Mailing List: [container-tools@redhat.com](https://www.redhat.com/mailman/listinfo/container-tools)
