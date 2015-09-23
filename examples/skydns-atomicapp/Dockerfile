FROM projectatomic/atomicapp:0.1.11

MAINTAINER langdon <langdon@fedoraproject.org>

LABEL io.projectatomic.nulecule.providers="kubernetes" \
      io.projectatomic.nulecule.specversion="0.0.2" \
      Build="docker build --rm --tag test/skydns-atomicapp ."

ADD Nulecule /application-entity/
ADD artifacts/ /application-entity/artifacts/
