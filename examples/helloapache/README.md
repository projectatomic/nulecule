# helloapache

This is an atomic application based on the nulecule specification. Kubernetes and native docker are currently the only supported providers. You'll need to run this from a workstation that has the atomic command.  If you wish to use the kubernetes provider, you will also need a kubectl client that can connect to a kubernetes master.

It's a single container application based on the centos/httpd image, but you can use your own.

## Option 1: Non-interactive defaults

Run the image. It will automatically use kubernetes as the orchestration provider.
```
[sudo] atomic run projectatomic/helloapache
```

Note: This option is not interactive because all params in the Nulecule file have default values.

## Option 2: Unattended

1. Create the file `answers.conf` with these contents:

    This sets up the values for the two configurable parameters (image and hostport) and indicates that kubernetes should be the orchestration provider.

        [general]
        provider = kubernetes

        [helloapache-app]
        image = centos/httpd # optional: choose a different image
        hostport = 80        # optional: choose a different port to expose
1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/helloapache
        ...
        helloapache


1. As an additional experiment, remove the kubernetes pod and change the provider to 'docker' and re-run the application to see it get deployed on base docker.

## Option 3: Install and Run

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
