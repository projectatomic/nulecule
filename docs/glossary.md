# Nulecule Glossary

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

