# Composite Container-based Application Specification

`\ˈnü-li-ˌkyül\` (n.) a made-up word meaning ["the mother of all atomic particles"](http://simpsons.wikia.com/wiki/Made-up_words).

**Your installer for container-based applications.** Replace your shell script and deployment instructions with some metadata.

**Change runtime parameters for different environments.** No need to edit files before deployment. Users can choose interactive or unattended deployment. Guide web interface users with parameter metadata to validate user input and provide descriptive help.

**Bridge between Enterprise IT and PaaS** With pluggable orchestration providers you can package your application to run on OpenShift, Kubernetes, Docker Compose, Helios, Panamax, Docker Machine, etc. and allow the user to choose the target when deployed.

**Compose applications from a catalog.** No need to re-package common services. Create composite applications by referencing other Nulecule-compliant apps. For example, adding a well-designed, orchestrated database is simply a reference to another container image.

## Problem Statement
Currently there is no standard way of defining a multi-container application's configuration without distributing instructions and files to the end-user. Additionally, these files must be managed and distributed via different systems than the containers themselves.

## What is Nulecule?

Nulecule defines a pattern and model for packaging complex multi-container applications and services, referencing all their dependencies, including orchestration metadata in a container image for building, deploying, monitoring, and active management.

The Nulecule specification enables complex applications to be defined, packaged and distributed using standard container technologies. The resulting container includes dependencies, supports multiple orchestration providers, and has the ability to specify resource requirements. The Nulecule specification also supports the aggregation of multiple composite applications. The Nulecule specification is container and orchestration agnostic, enabling the use of any container and orchestration technology.

**[Glossary of terms](docs/glossary.md)**

## Nulecule Specification Highlights

* Application description and context maintained in a single container through extensible metadata
* Composable definition of complex applications through inheritance and composition of containers into a single, standards-based, portable description.
* Simplified dependency management for the most complex applications through a directed graph to reflect relationships.
* Container and orchestration engine agnostic, enabling the use of any container technology and/or orchestration technology

## “The Big Picture”

![Alt Nulecule specification high-level story.](/images/NuleculeHigh-LevelStory.png "Nulecule specification high-level story")

## Deployment User Experience

The Nulecule specification has been implemented in the [Atomic App reference implementation](https://github.com/projectatomic/atomicapp).  Atomic App currently supports docker containers and kubernetes and docker orchestration providers.  The [atomic command](https://github.com/projectatomic/atomic) is used to run the container that contains the Nulecule specification and the Atomic App implementation.

This example is a single container application based on the centos/httpd image, but you can use your own.

You may wish to run the nulecule from an empty directory as it will copy the nulecule files to the working directory for inspection everytime it is run.

### Option 1: Non-interactive defaults

Run the image. It will automatically use kubernetes as the orchestration provider.  This will become interactive and prompt for defaults if the Nulecule file doesn't provide defaults for all of the parameters.

```
[sudo] atomic run projectatomic/helloapache
```

### Option 2: Unattended

1. Create the file `answers.conf` with these contents:

    This sets up the values for the two configurable paramaters (image and hostport) and indicates that kubernetes should be the orchestration provider.

        [general]
        provider = kubernetes

        [helloapache-app]
        image = centos/httpd # optional: choose a different image
        hostport = 80        # optional: choose a different port to expose
1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/helloapache
        ...
        helloapache


1. As an additional experiment, remove the kubernetes pod and change the provider to 'docker' and re-run the application to see it get deployed on native docker.

### Option 3: Install and Run

You may want to download the application, review the configuraton and parameters as specified in the Nulecule file, and edit the answerfile before running the application.

1. Download the application files using `atomic install`

        [sudo] atomic install projectatomic/helloapache

1. Rename `answers.conf.sample`

        mv answers.conf.sample answers.conf

1. Edit `answers.conf`, review files if desired and then run

        $ [sudo] atomic run projectatomic/helloapache
        ...
        helloapache

## Test
Any of these approaches should create a kubernetes pod or a running docker container. 

With a kubernetes pod, once its state is "Running" curl the minion it's running on.

```
$ kubectl get pod helloapache
POD                IP                  CONTAINER(S)       IMAGE(S)           HOST                LABELS              STATUS
helloapache        172.17.0.8          helloapache        centos/httpd       10.3.9.216/         name=helloapache   Running
$ curl 10.3.9.216
<bunches_of_html_goodness>
```

If you test the docker provider, once the container is running, curl the port on your localhost.

```
$ curl localhost
<bunches_of_html_goodness>
```

Additional examples are available in the [examples](examples/) directory.

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
