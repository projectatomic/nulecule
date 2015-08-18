This is the [guestbook-go](https://github.com/GoogleCloudPlatform/kubernetes/tree/master/examples/guestbook-go) sample application from the kubernetes project, packaged as an atomic application based on the nulecule specification. 

Kubernetes is currently the only supported provider. You'll need to run this from a workstation that has the atomic CLI and kubectl client that can connect to a kubernetes master. This example depends on kube-dns being configured on your kubernetes cluster.

### Step 1

Build:

```
# docker build -t $USER/guestbookgo-atomicapp .
```

### Step 2 

Install and Run:


```
# atomic install $USER/guestbookgo-atomicapp
# atomic run $USER/guestbookgo-atomicapp
```

### Step 3

Access the guestbook through a random NodePort on your cluster. Find the port by running:

```
$ kubectl describe service guestbook | grep NodePort

NodePort:		<unnamed>	31288/TCP
```

To find the ip address on your node, run:

```
$ kubectl get nodes
NAME          LABELS                               STATUS
kube-node-1   kubernetes.io/hostname=kube-node-1   Ready
```

And using the node name from above, run:

```
$ kubectl describe nodes kube-node-1 | grep Addresses
Addresses:	192.168.121.174
```

Once the app's container images are pulled and pods are running, you'll be able to reach the guestbook:

```
curl 192.168.121.174:31288
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta charset="utf-8">
    <meta content="width=device-width" name="viewport">
    <link href="/style.css" rel="stylesheet">
    <title>Guestbook</title>
  </head>
...
``` 
