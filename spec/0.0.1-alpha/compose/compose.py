#!/usr/bin/env python

import logging
import os
import json
import urllib2
import tempfile
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter


logging.basicConfig()
logger = logging.getLogger("compose")
logger.setLevel(logging.INFO)

MAIN_FILE = "Atomicfile"

class Compose(object):
    schema_url = None
    __schema_path = None
    __schema_dir = None
    __schema = None
    __tmpdir = None

    @property
    def tmpdir(self):
        if not self.__tmpdir:
            self.__tmpdir = tempfile.mkdtemp(prefix="nulecule-spec-") 
            logger.info("Using temporary directory %s" % self.__tmpdir)

        return self.__tmpdir

    @property
    def schema_dir(self):
        if not self.__schema_dir:
            if self.schema_url:
                self.__schema_dir = os.path.dirname(self.schema_path)
            else:
                self.__schema_dir = os.path.abspath(os.path.dirname(self.schema_path))
            logger.debug("Setting 'schema_dir' to %s" % self.__schema_dir)
        return self.__schema_dir

    @property
    def schema_path(self):
        if not self.__schema_path:
            self.__schema_path, _ = self.download(self.schema_url)
            logger.debug("Setting 'schema_path to %s" % self.__schema_path)
        return self.__schema_path

    @schema_path.setter
    def schema_path(self, path):
        self.__schema_path = path
        logger.debug("Schema path is %s" % os.path.dirname(path))

    @property
    def schema(self):
        if not self.__schema:
            self.__schema = self.loadSchema(self.schema_path)
        return self.__schema

    def __init__(self, schema):
        if os.path.isfile(schema):
            self.schema_path = schema
        else:
            logger.debug("Given schema is not stored locally")
            self.schema_url = schema
        
    def loadSchema(self, schema_path):
        if not os.path.isfile(schema_path):
            raise Exception("Path to schema %s does not exist" % schema_path)

        content = None
        with open(schema_path, "r") as fp:
            content = json.load(fp)

        if not content:
            raise Exception("Couldn't load content of %s" % schema_path)

        return content

    def download(self, url):
        data = self.getData(url)
        output_name = os.path.basename(url)
        path = os.path.join(self.tmpdir, output_name)
        with open(path, "w") as fp:
            fp.write(data)

        return path, data

    def getUrl(self, ref):
        path = None
        if self.schema_url:
            path = os.path.join(os.path.dirname(self.schema_url), ref)
        else:
            path = "file://%s" % os.path.join(self.schema_dir, ref)

        return path

    def getData(self, ref):
        logger.debug("Loading data for %s" % ref)
        try:
            ref_data = urllib2.urlopen(ref)
        except ValueError:
            ref = self.getUrl(ref)
            logger.debug("Real path to load from is %s" % ref)
            ref_data = urllib2.urlopen(ref)

        return ref_data.read()

    def getRefObject(self, ref_data):
        return json.loads(ref_data)

    def composeSchema(self, data):
        for name, contents in data.iteritems():
            if "ref" in contents:
                logger.info("Pulling content for %s from %s" % (name, contents["ref"]))
                _, ref_data = self.download(contents["ref"])
                contents.update(self.getRefObject(ref_data))
                del contents["ref"]
            if "value" in contents and contents["value"]:
                if type(contents["value"]) == dict:
                    self.composeSchema(contents["value"])
                elif type(contents["value"]) == list:
                    for item in contents["value"]:
                        if type(item) == dict:
                            self.composeSchema(item)

    def writeSchema(self, output_file):
        with open(output_file, "w") as fp:
            fp.write(self.serializeSchema())

    def serializeSchema(self):
        return json.dumps(self.schema,sort_keys=True, indent=4, separators=(',', ': '))

    def run(self, output_file=None):
        main_schema = None

        for element in self.schema["elements"]:
            if type(element["contents"]) is dict:
                main_schema = element["contents"]
                self.composeSchema(main_schema)

        if output_file:
            self.writeSchema(output_file)
        else:
            print(self.serializeSchema())

        

def main():
    parser = ArgumentParser(description='This tool lets you compose schema containing references into a single file', formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("SCHEMA", help="Path/URL to the main schema file")
    parser.add_argument("--output", dest="output", help="Path to a file which will containt composed schema file if the composition succeedes")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", dest="verbose", help="Make the output more verbose")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    comp = Compose(args.SCHEMA)
    comp.run(args.output)

if __name__ == '__main__':
    main()
