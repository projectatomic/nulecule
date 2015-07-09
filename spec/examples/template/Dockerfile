FROM goern/atomicapp-centos7 

MAINTAINER Christoph Görn <goern@redhat.com>

# these two are equivalent
LABEL Version v1.0.0 # this is used by atomic tool 

# a namespaced metadata expressed as Dockerfile LABELs
LABEL io.projectatomic.nulecule.specversion 0.0.2

ADD /Nulecule /Dockerfile /application-entity/
ADD /artifacts /application-entity/artifacts

