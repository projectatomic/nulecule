# Build

```
[sudo] docker build -t projectatomic/sentry .
```

# Run

- Copy ``answers.conf.sample`` to ``answers.conf`` and customize as needed.

```
[sudo] atomic run projectatomic/sentry
```

Run ``kubectl get pods`` to check if the pods for ``redis``, ``postgres``
and ``sentry`` are up and running.

Check info for ``sentry`` service.

```
$ kubectl get services sentry
NAME      LABELS        SELECTOR      IP(S)           PORT(S)
sentry    name=sentry   name=sentry   10.254.131.20   9000/TCP
```


# Usage

- Setup sentry: ``kubectl exec -ti sentry sentry upgrade``

- Open ``http://10.254.131.20:9000`` in browser to access Sentry.
