This is an atomicapp application based on the nulecule specification. Docker and Kubernetes are the supported providers. You'll need to run this from a workstation that has the [atomic](https://github.com/projectatomic/atomic) command and kubectl client that can connect to a kubernetes master.

It is 3 a tier application based on redis, postgresql and gitlab. This is also an example Nulecule having multiple tier artifacts rather using graphs.

### Option 1: Interactive

Run the image. It will automatically use kubernetes as the orchestration provider.  It will prompt for all parameters in the Nulecule file that do not have default values:

    $ [sudo] atomic run projectatomic/gitlab-centos7-atomicapp

## Option 2: Unattended

1. Create the file `answers.conf` with these contents:

    This sets up the values for the configurable parameters and indicates that kubernetes should be the orchestration provider.

        [general]
        namespace = default
        provider = kubernetes

        [redis]
        image=swordphilic/redis:latest

        [postgresql]
        image=swordphilic/postgresql:latest
        # following params are used for Docker provider
        DB_USER=gitlab
        DB_PASS=password
        DB_NAME=gitlab_production


        [gitlab]
        image=swordphilic/gitlab:latest
        DB_USER=gitlab
        DB_PASS=password
        DB_NAME=gitlab_production
        # port on the node where Gitlab over HTTP will be accessible - valid range 30000-32667
        NODE_PORT=30000


1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/gitlab-centos7-atomicapp

### Option 3: Install and Run

You may want to download the application, review the configuraton and parameters as specified in the Nulecule file, and edit the answerfile before running the application.

1. Download the application files using `atomic install`

        [sudo] atomic install projectatomic/gitlab-centos7-atomicapp

1. Rename `answers.conf.sample`

        mv answers.conf.sample answers.conf

1. Edit `answers.conf`, review files if desired and then run

        $ [sudo] atomic run projectatomic/gitlab-centos7-atomicapp

Note: You can change the provider to `docker` and the app will be deployed using `docker`.

## Test
Any of these approaches should create kubernetes replication controllers, pods and services.

Gitlab is web app, to test if its functioning we can access it in browser.
We have configured the app on ADB port 30000 (see answer.conf). You can access
the app using the IP of ADB box at port 30000 or by forwarding the port 30000 of ADB box to
host machine port.

To test out if app is running and intialized properly (run following inside ADB)
```
$ kubectl get pods
NAME               READY     STATUS    RESTARTS   AGE
gitlab-0nax4       1/1       Running   0          15m
postgresql-ytsy5   1/1       Running   0          15m
redis-s5cge        1/1       Running   0          15m

$ kubectl logs gitlab-0nax4
which: no docker in
(/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin)
which: no docker in
(/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin)
Generating SSH2 RSA host key: [  OK  ]
Generating SSH2 ECDSA host key: [  OK  ]
Generating SSH2 ED25519 host key: [  OK  ]
Waiting for database server to accept connections
Setting up GitLab for firstrun. Please be patient, this could take a while...
PG::Error: ERROR:  new encoding (UTF8) is incompatible with the encoding of the
template database (SQL_ASCII)
HINT:  Use the same encoding as in the template database, or use template0 as
template.
: CREATE DATABASE "gitlab_production" ENCODING = 'unicode'
[..]
Couldn't create database for {"adapter"=>"postgresql", "encoding"=>"unicode",
"database"=>"gitlab_production", "host"=>"10.254.213.29", "port"=>5432,
"username"=>"gitlab", "password"=>"password", "pool"=>10}
Migrating database...
Compiling assets. Please be patient, this could take a while...
Starting supervisord...
2015-09-08 12:09:17,509 CRIT Supervisor running as root (no user in config
file)
2015-09-08 12:09:17,509 WARN Included extra file "/etc/supervisord.d/cron.ini"
during parsing
2015-09-08 12:09:17,509 WARN Included extra file "/etc/supervisord.d/nginx.ini"
during parsing
2015-09-08 12:09:17,509 WARN Included extra file
"/etc/supervisord.d/sidekiq.ini" during parsing
2015-09-08 12:09:17,509 WARN Included extra file "/etc/supervisord.d/sshd.ini"
during parsing
2015-09-08 12:09:17,509 WARN Included extra file
"/etc/supervisord.d/unicorn.ini" during parsing
2015-09-08 12:09:17,569 INFO RPC interface 'supervisor' initialized
2015-09-08 12:09:17,569 CRIT Server 'unix_http_server' running without any HTTP
authentication checking
2015-09-08 12:09:17,576 INFO supervisord started with pid 1
2015-09-08 12:09:18,581 INFO spawned: 'sidekiq' with pid 307
2015-09-08 12:09:18,584 INFO spawned: 'unicorn' with pid 308
2015-09-08 12:09:18,590 INFO spawned: 'cron' with pid 309
2015-09-08 12:09:18,594 INFO spawned: 'nginx' with pid 310
2015-09-08 12:09:18,597 INFO spawned: 'sshd' with pid 311
2015-09-08 12:09:19,993 INFO success: sidekiq entered RUNNING state, process
has stayed up for > than 1 seconds (startsecs)
2015-09-08 12:09:19,993 INFO success: unicorn entered RUNNING state, process
has stayed up for > than 1 seconds (startsecs)
2015-09-08 12:09:19,993 INFO success: cron entered RUNNING state, process has
stayed up for > than 1 seconds (startsecs)
2015-09-08 12:09:19,993 INFO success: nginx entered RUNNING state, process has
stayed up for > than 1 seconds (startsecs)
2015-09-08 12:09:19,993 INFO success: sshd entered RUNNING state, process has
stayed up for > than 1 seconds (startsecs)

```

To forward port `30000` of ADB box to host machine port `30000`, add following line your Vagrantfile

```
config.vm.network "forwarded_port", guest: 30000, host: 30000, auto_correct: true

```

and run following command to apply changes in updated Vagrantfile

```
vagrant reload
```

Observe logs as shown above if app is configured and ready to accept connections, once it is ready you should be able to access the app at host browser using address

```
http://127.0.0.1:30000
```

For first time login you can use following credentials:

 - username: root
 - password: 5iveL!fe
