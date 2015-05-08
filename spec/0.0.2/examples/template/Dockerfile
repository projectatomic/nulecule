FROM goern/atomicapp-centos7 

MAINTAINER Christoph Görn <goern@redhat.com>

# these two are equivalent
LABEL Version v1.0.0 # this is used by atomic tool 
LABEL Nulecule/appversion v1.0.0 # and that would be new

# actually we can infer the type of the generated docker image from the presence of Nulecule/specversion
LABEL Type Nulecule

# this is close to https://github.com/openshift/origin/blob/f3711ec305e0fbdf8ef58e2e65cfc30753d526d5/docs/proposals/metadata.md
# a namespaced metadata expressed as Dockerfile LABELs
LABEL Nulecule/specversion 0.0.2

ADD /Nulecule /Dockerfile /application-entity/
ADD /artifacts /application-entity/artifacts

