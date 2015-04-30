# Schema Composer
Nulecule spec provides schema in json format which servers as a machine readable alternative to textual specification. To make the schema more consumable we've split it to multiple file representing objects in specification (`GraphObject`, `MetadataObject`, etc.). The purpose of this tool is to compose these separate objects into one giant json file representing whole schema. 

Objects are referenced by option with key `ref`. The value of `ref` can be relative path or URL.

## How to Use
```
usage: compose.py [-h] [--output OUTPUT] [-v] SCHEMA

This tool lets you compose schema containing references into a single file

positional arguments:
  SCHEMA           Path/URL to the main schema file

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Path to a file which will containt composed schema file if
                   the composition succeedes
  -v, --verbose    Make the output more verbose
```

### Example

Schema can be specified by URL which means for all references which paths are specified as relative will be prefixed with the url to the main schema file.
```
compose.py https://raw.githubusercontent.com/vpavlin/nulecule/master/spec/0.0.1-alpha/schema.json --output composed_schema.json -v
```

You can run the tool also on local files. Similarly to the example above - all relative paths in references will be prefixed with absolute path to the directory schema.json lives in
```
compose.py schema.json --output composed_schema.json -v
```

