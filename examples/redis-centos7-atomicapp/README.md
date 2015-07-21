# redis-centos7-atomicapp

This is a redis sample application, in which redis master and slave components are packaged as an atomic application based on the nulecule specification. 

Kubernetes and native docker are currently the only supported providers. You'll need to run this from a workstation that has the atomic command.  If you wish to use the kubernetes provider, you will also need a kubectl client that can connect to a kubernetes master.

## Option 1: Non-interactive defaults

Run the image. It will automatically use kubernetes as the orchestration provider.

    $ [sudo] atomic run projectatomic/redis-centos7-atomicapp

Note: This option is not interactive because all params in the Nulecule file have default values.

## Option 2: Unattended

1. Create the file `answers.conf` with these contents:

    This changes the port for the master from the default of 6379 to 16379. and indicates that kubernetes should be the orchestration provider.

    [general]
    namespace = default
    provider = kubernetes
    [redismaster-app]
    hostport = 16379
    [redisslave-app]
    master_hostport = 16379

1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/redis-centos7-atomicapp

1. As an additional experiment, remove the kubernetes pod and change the provider to 'docker' and re-run the application to see it get deployed on base docker.

## Option 3: Install and Run

You may want to download the application, review the configuraton and parameters as specified in the Nulecule file, and edit the answerfile before running the application.

1. Download the application files using `atomic install`

        $ [sudo] atomic install projectatomic/redis-centos7-atomicapp

1. Rename `answers.conf.sample`

        mv answers.conf.sample answers.conf

1. Edit `answers.conf`, review files if desired and then run

        $ [sudo] atomic run projectatomic/redis-centos7-atomicapp

## Test
Any of these approaches should create a kubernetes service or a pair of running docker containers. 

With a kubernetes service, once its pods are in the "Running" state, you can use the redis-cli to access the server.  The example below uses the `redis-cli` in the redis container.

```
$ kubectl get service redis-master
NAME           LABELS                   SELECTOR                 IP              PORT(S)
redis-master   name=redis,role=master   name=redis,role=master   <IP Address>    <port>/TCP
$ docker run --rm -it jasonbrooks/redis redis-cli -h <IP Address> -p <port>
<IP Address>:<port>> get key
(nil)
<IP Address>:<port>> set key value
OK
<IP Address>:<port>> get key
"value"
<IP Address>:<port>> del key
(integer) 1
<IP Address>:<port>> get key
(nil)
<IP Address>:<port>> exit
```

Clean up can be accomplished by deleting the pods, service, and replication controllers as follows:

    $ kubectl delete pod,rc,svc -l name=redis
