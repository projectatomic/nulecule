# Getting Started with Nulecule

You have an application you want to package up as a Nulecule for distribution. It's composed of one or more containers that together link to provide your application.

## Plan
1. Determine what components of your application are custom and which are "stock" parts.  For example, do you need a custom web server, or do you just need to load a specific configuration onto an already packaged web server.
1. Find your resources. 
    - **nulecule applications** Are there existing Nulecule Applications you can leverage in your own application?
    - **container images** Carefully consider if you really need to build your own containers.  For example, do you really need your own web server or database image? If you're writing a Dockerfile for a common service, try to find a well-known, supported, certified, stable image that you can build on.
    - **provider orchestration templates** When you are considering how to provide configuration for orchestration providers, such as kubernetes files (service, replication controller, pod) or OpenShift or Docker Compose files, see if you can use exising templates or known good files. As with container images, if you're writing files for common services, try to find well-known, supported, certified, stable templates that you can build on.

## Prepare
From the planning phase, you've got a collection of remote and local sources that your application will be comprised of.

1. Start with the containers. Understand how they run standalone. Get them running.  Make sure the entire application runs manually.
1. Orchestrate the containers on the target provider. Start simply and build up. For example, with kubernetes just deploy as a pod. Once that succeeds, add a service, and then some replication controllers. There are many opportunities for error -- so make small changes, test and iterate slowly. Verify your [YAML](http://codebeautify.org/yaml-validator) or [JSON](http://jsonlint.com/) frequently. Use a method that can be easily incorporated into your development workflow: small change -> save -> validate -> test -> rinse and repeat.
1. Test both custom and stock services together. Nulecule won't do magical things. The pieces must all work together before they can be packaged up as a unit.

## Package
Only when everything is working are you ready to package the application. In this phase you'll be interacting with the [Nulecule specification](/spec).

1. Download a [Nulecule template](/spec/examples/template) to start from.
1. In the Nulecule file, create one or more lists of things under `graph`. These represent the different components that make up your application. Names are arbitrary. Remember to verify your [YAML](http://codebeautify.org/yaml-validator) or [JSON](http://jsonlint.com/) frequently.

    1. If your sources are remote, then all that is needed is a name and source. Remote sources are other Nulecule applications.

            graph:
            - name: mydb
              source: "docker://registry.example.com/some/database"
    1. If your sources are local, then provide a name and an artifacts key that will reference the source file(s). Each provider will have a key specifying the provider. For example, "docker" or "kubernetes".

            graph:
            - name: myapp
              artifacts:
                kubernetes:
                  - file:///artifacts/kubernetes/pod.json
                  - file:///artifacts/kubernetes/service.json

1. Put all of the provider files into a directory structure that corresponds to the provider artifacts section in the Nulecule file. Using the above example, `artifacts/kubernetes/<file>.json`. The structure should resemble something like this:

        ├── Dockerfile
        ├── artifacts
        │   └── kubernetes
        │       ├── pod.json
        │       └── service.json
        ├── Nulecule
        └── README.md

1. Consider the different ways your application may be deployed. There will likely be many parameters that need to be exposed at deployment. It's best to overdo this and provide defaults whenever possible. Go through the provider files and change any values. For example `database_pass: changeme` becomes `database_pass: $db_pass`. The name of the parameter is `db_pass`. These go into the params section of the Nulecule file under each provider. For example:


        graph:
        - mydb:
          ...
          params:
          - name: db_pass
            description: database passphrase
          - name: port
            description: frontend TCP port
            default: 80

1. Consider any additional information that is useful for deployment. Write a README file focused on deployment. Use a popular format such as Markdown or asciidoc so it can be read from a terminal window or rendered in a graphical interface.
    * what does this application do?
    * what provider environment(s) do I need to have setup before I deploy it?
    * how do I verify that it has been deployed correctly?

1. Add a metadata section, including a name, description and license information. Arbitrary metadata may also be added. Consider using keyword tags that may be useful for deployment management. For example:

        metadata:
          name: My Cool App
          appversion: 1.0.0
          description: Lorem ipsum dolor sit amet, consectetur adipiscing elit
          license:
            name: GPLv3
            url: http://www.example.com/license
          tags:
            - foo
            - bar

1. Before packaging up into a container, try running it in a test mode if one is provided by your Nulecule implementation.  If you are using the [Atomic App reference implementation](https://github.com/projectatomic/atomicapp), use the `dry-run` and `verbose` options as follows: `atomicapp --dry-run --verbose run`. This should output the commands that will run. Common errors:
    * provider files don't match the artifact relative path
    * yaml or json is not valid
    * missing parameter

1. Once the Nulecule file and provider artifacts are working, package the application as a container. Typically, this means basing it off of an executable image provided by the implementation of Nulecule you are using.  If you are using the [Atomic App reference implementation](https://github.com/projectatomic/atomicapp), the stock Dockerfile may be used, unaltered, unless you have a special use case.

        [sudo] docker build -t mydb-app .

## Push & Pull
Push the image to a registry. Tell people about it and see if they can deploy your application without any assistance. If they have questions, you probably should enhance the application and parameter descriptions so they are clear.
