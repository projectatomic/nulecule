This is an atomic application based on the nulecule specification. Kubernetes and native docker are currently the only supported providers. You'll need to run this from a workstation that has the atomic command and kubectl client that can connect to a kubernetes master.

It's a single container application based on the centos/mariadb image.

### Option 1: Interactive

Run the image. It will automatically use kubernetes as the orchestration provider.  It will prompt for all parameters in the Nulecule file that do not have default values.  These are "db_user", "db_password", and "db_name"

    $ [sudo] atomic run projectatomic/mariadb-centos7-atomicapp

## Option 2: Unattended

1. Create the file `answers.conf` with these contents:

    This sets up the values for the two configurable parameters (image and hostport) and indicates that kubernetes should be the orchestration provider.

        [general]
        provider = kubernetes

        [mariadb-atomicapp]
        db_user = username
        db_pass = password
        db_name = dbname

1. Run the application from the current working directory

        $ [sudo] atomic run projectatomic/mariadb-centos7-atomicapp

1. As an additional experiment, remove the kubernetes pod and change the provider to 'docker' and re-run the application to see it get deployed on native docker.

### Option 3: Install and Run

You may want to download the application, review the configuraton and parameters as specified in the Nulecule file, and edit the answerfile before running the application.

1. Download the application files using `atomic install`

        [sudo] atomic install projectatomic/mariadb-centos7-atomicapp

1. Rename `answers.conf.sample`

        mv answers.conf.sample answers.conf

1. Edit `answers.conf`, review files if desired and then run

        $ [sudo] atomic run projectatomic/mariadb-centos7-atomicapp

## Test
Any of these approaches should create a kubernetes pod and service.

You can test it using the `mariadb` command in the centos/mariadb container.

```
$ kubectl get service mariadb
NAME      LABELS    SELECTOR       IP               PORT(S)
mariadb   name=db   name=mariadb   10.254.167.159   3306/TCP

$ docker run -it centos/mariadb mysql -h <IP address> -u <username> -p <database name>
Enter password: <password>
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.0.17-MariaDB MariaDB Server

Copyright (c) 2000, 2015, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [dbname]> show databases;
+--------------------+
| Database           |
+--------------------+
| dbname             |
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
5 rows in set (0.00 sec)
```
