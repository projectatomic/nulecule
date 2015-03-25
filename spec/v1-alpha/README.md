## Atomicfile

```
{
  "name": String,
  "appversion": String,
  "graph": [ String ],
  "save_answers": Boolean
}
```

## params.ini

```
[general]


[app1]
```

## Directory Layout

```
├── Atomicfile
├── init
│   └── dbapp
│       └── run.sh
├── kubernetes
│   ├── app1
│   │   ├── pod.json
│   │   ├── replication_controller.json
│   │   └── service.json
│   └── app2
│       ├── pod.json
│       ├── replication_controller.json
│       └── service.json
└── params.ini

```
