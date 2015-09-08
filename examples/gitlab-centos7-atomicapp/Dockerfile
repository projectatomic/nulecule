FROM projectatomic/atomicapp:0.1.3

MAINTAINER Navid Shaikh <nshaikh@redhat.com>

LABEL io.projectatomic.nulecule.specversion="0.0.2" \
      io.projectatomic.nulecule.providers="kubernetes"\
      Build="docker build --rm --tag swordphilic/gitlab-atomicapp ."

ADD /Nulecule /Dockerfile README.md gpl-3.0.txt /application-entity/
ADD /artifacts /application-entity/artifacts
