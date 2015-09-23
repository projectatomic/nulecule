FROM projectatomic/atomicapp:0.1.11

MAINTAINER Christoph Görn <goern@redhat.com>

LABEL io.projectatomic.nulecule.specversion="0.0.2" \
      io.projectatomic.nulecule.providers="kubernetes, openshift" \
      Build="docker build --rm --tag test/wordpress-centos7-atomicapp ."

ADD /Nulecule /Dockerfile README.asciidoc gpl-3.0.txt /application-entity/
ADD /artifacts /application-entity/artifacts
