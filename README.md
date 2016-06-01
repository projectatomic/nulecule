# Composite Container-based Application Specification

`\ˈnü-li-ˌkyül\` (n.) a made-up word meaning ["the mother of all atomic particles"](http://simpsons.wikia.com/wiki/Made-up_words).

**Your installer for container-based applications.** Replace your shell script and deployment instructions with some metadata.

**Change runtime parameters for different environments.** No need to edit files before deployment. Users can choose interactive or unattended deployment. Guide web interface users with parameter metadata to validate user input and provide descriptive help.

**Bridge between Enterprise IT and PaaS** With pluggable orchestration providers you can package your application to run on OpenShift, Kubernetes, Docker Compose, Helios, Panamax, Docker Machine, etc. and allow the user to choose the target when deployed.

**Compose applications from a catalog.** No need to re-package common services. Create composite applications by referencing other Nulecule-compliant apps. For example, adding a well-designed, orchestrated database is simply a reference to another container image.

## Problem Statement
Currently there is no standard way of defining a multi-container application's configuration without distributing instructions and files to the end-user. Additionally, these files must be managed and distributed via different systems than the containers themselves.

Containers in the OCI (Open Container Initiative) format derived from Docker offers a new approach for application packaging. OCI enables application-centric aggregate packaging, optimized for deployment into containers. However most applications will consist of multiple containers, which surfaces two issues: the relationships between containers need to be expressed in order to manage dependencies and orchestrate the deployment (e.g. set up network connections) with consideration of environmental factors, and this application-level meta-data needs to be distributed. OCI itself, however, stops at the individual container. Orchestration tools such as Kubernetes offer a generic description model for multi-container applications, however they do not define a transport model, nor a standard way to parameterize a generic template. The mindset of most, if not all, current container orchestration systems is to treat the aggregate, multi-container application as state of the cluster rather than an entity in it's own right and therefore they regress beyond the portability that OCI introduced. This means that it's very easy to put a individual service into a Docker-style Registry, however there is no way to represent a full application at the distribution level - I can create a single MariaDB container, but not a MariaDB/Galera cluster or even a full application such as [Kolab](https://kolab.org/). So what is missing? A standard way to describe and package a multi-container application.

## What is Nulecule?

Nulecule defines a pattern and model for packaging complex multi-container applications and services, referencing all their dependencies, including orchestration metadata in a container image for building, deploying, monitoring, and active management.

The Nulecule specification enables complex applications to be defined, packaged and distributed using standard container technologies. The resulting container includes dependencies, supports multiple orchestration providers, and has the ability to specify resource requirements. The Nulecule specification also supports the aggregation of multiple composite applications. The Nulecule specification is container and orchestration agnostic, enabling the use of any container and orchestration technology.

**[Glossary of terms](docs/glossary.md)**

## Specification

An actively maintained page on the specifics of the specification can be found at [SPECIFICATION.md](SPECIFICATION.md).

## Nulecule Specification Highlights

* Application description and context maintained in a single container through extensible metadata
* Composable definition of complex applications through inheritance and composition of containers into a single, standards-based, portable description.
* Simplified dependency management for the most complex applications through a directed graph to reflect relationships.
* Container and orchestration engine agnostic, enabling the use of any container technology and/or orchestration technology

## “The Big Picture”

![Alt Nulecule specification high-level story.](/images/NuleculeHigh-LevelStory.png "Nulecule specification high-level story")

## Deployment User Experience

The Nulecule specification has been implemented in the [Atomic App reference implementation](https://github.com/projectatomic/atomicapp).  Atomic App currently supports docker as well as container orchestrators such as Kubernetes, OpenShift and Marathon.  The [atomic](https://github.com/projectatomic/atomic) or [atomicapp](https://github.com/projectatomic/atomicapp] command is used to run the container that contains the Nulecule specification.

## Getting started on Nulecule with Atomic App

Nulecule can use the Atomic App implementation which can be used either natively on your OS __or__ ran via the [atomic](https://github.com/projectatomic/atomic) command on [Fedora or CentOS Atomic hosts](https://www.projectatomic.io/download/).

__Detailed instructions on [getting started](https://github.com/projectatomic/atomicapp/blob/master/docs/start_guide.md) are available.__ Alternatively, use the [quick start guide](https://github.com/projectatomic/atomicapp/blob/master/docs/quick_start.md) to get a Nuleculized application running immediately.

This example is a single container application based on the centos/httpd image, but you can use your own.

A quick example of this being used are launching the `projectatomic/helloapache` example:

```bash
▶ sudo atomicapp run projectatomic/helloapache --destination helloapache
INFO   :: Atomic App: 0.5.2 - Mode: Run
INFO   :: Unpacking image projectatomic/helloapache to helloapache
INFO   :: Skipping pulling docker image: projectatomic/helloapache
INFO   :: Extracting Nulecule data from image projectatomic/helloapache to helloapache
INFO   :: App exists locally and no update requested
INFO   :: Using namespace default
INFO   :: trying kubectl at /usr/bin/kubectl
INFO   :: trying kubectl at /usr/local/bin/kubectl
INFO   :: found kubectl at /usr/local/bin/kubectl
INFO   :: Deploying to Kubernetes

Your application resides in helloapache
Please use this directory for managing your application

▶ kubectl get po
NAME                   READY     STATUS    RESTARTS   AGE
helloapache            1/1       Running   0          6s
k8s-etcd-127.0.0.1     1/1       Running   0          20d
k8s-master-127.0.0.1   4/4       Running   0          23h
k8s-proxy-127.0.0.1    1/1       Running   0          23h
```

## Developer User Experience

See the [Getting Started with Nulecule guide](GETTING_STARTED.md).

## Implementations

This is only a specification. Implementations may be written in any language. See [implementation guide](IMPLEMENTATION_GUIDE.md) for more details.

**Reference implementation:** https://github.com/projectatomic/atomicapp

## Examples / Library

For a library of examples conforming to the current reference implementation [atomicapp](https://github.com/projectatomic/atomicapp) please visit [github.com/projectatomic/nulecule-library](https://github.com/projectatomic/nulecule-library)

### Developer tooling

Developer tooling is TBD. There is some work planned for [DevAssistant](http://devassistant.org/).

### Contributing

Please review the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

###Communication channels

* IRC: #nulecule (On Freenode)
* Mailing List: [container-tools@redhat.com](https://www.redhat.com/mailman/listinfo/container-tools)

## Copyright

Copyright (C) 2016 Red Hat Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

The GNU General Public License is provided within the file [LICENSING](LICENSING).
