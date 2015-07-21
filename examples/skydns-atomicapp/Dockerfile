FROM projectatomic/atomicapp:0.1.0

MAINTAINER langdon <langdon@fedoraproject.org>

LABEL io.projectatomic.nulecule.providers = "kubernetes"
LABEL io.projectatomic.nulecule.specversion 0.0.2

LABEL Build docker build --rm --tag testing/skydns-atomicapp .


ADD Nulecule /application-entity/
ADD artifacts/ /application-entity/artifacts/
