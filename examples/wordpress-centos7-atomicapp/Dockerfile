FROM projectatomic/atomicapp:0.1.1

MAINTAINER Christoph Görn <goern@redhat.com>

LABEL io.projectatomic.nulecule.specversion 0.0.2
LABEL io.projectatomic.nulecule.providers "kubernetes, openshift"

LABEL Build docker build --rm --tag goern/wordpress-centos7-atomicapp .



ADD /Nulecule /Dockerfile README.asciidoc gpl-3.0.txt /application-entity/
ADD /artifacts /application-entity/artifacts

