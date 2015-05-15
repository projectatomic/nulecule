This is an atomic application based on the nulecule specification. Kubernetes is currently the only supported provider. You'll need to run this from a workstation that has the atomic CLI and kubectl client that can connect to a kubernetes master.

It's a single pod based on the centos/httpd image, but you can use your own.

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

## Test
Any of these approaches should create a kubernetes pod. Once its state is "Running" curl the minion it's running on.

```
$ kubectl get pod helloapache
POD                IP                  CONTAINER(S)       IMAGE(S)           HOST                LABELS              STATUS
helloapache        172.17.0.8          helloapache        centos/httpd       10.3.9.216/         name=helloapache   Running
$ curl 10.3.9.216
<bunches_of_html_goodness>
```
