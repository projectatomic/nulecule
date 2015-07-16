# Lifecycle of the Specification

This document and the processes it describes will become effective starting Nulecule Specification 0.0.2. It is valid until replaced by a newer version or noted otherwise.

## Normative Document

The normative Nulecule Specification document will be published at http://www.projectatomic.io/nulecule/spec/<major.minor.patch>/
Versioning is using the [semantic versioning scheme](http://semver.org/spec/v2.0.0.html).

In addition to the human readable HTML document, a JSON formated machine readable version of the specification will be published at the same URL path as the HTML document. The document name will be schema.json and may reference other files using the JSON DRAFT4 references.

The normative machine readable Nulecule Specification document will be published at https://github.com/projectatomic/nulecule/blob/v<major.minor.patch>/spec/<major.minor.patch>/schema.json

## States

The Nulecule Specification will have a certain set of releases, we will use semantic versioning to identify the releases.
Prior each release there will be a draft version of the release. This will be used to work/collaborate on the spec itself.

## Contributors and release process

Everybody is welcome to contribute to the draft version of the upcoming release. This will be documented by pull
requests (to the github repository of the Nulecule Specification) to the draft of the specification. Once a draft
has stabilized, it will be prepared by the specification maintainers and prepared for release. The maintainers
will release a new release of the specification.

### Changes to a Releases

Changes to released versions of the specification will not change the structure or feature set of the specification.
They are only meant to fix spelling or language errors, add or correct examples.

Collaboration on the draft of the next release of the Nulecule Specification will be done on the master branch of the github
repository of the Nulecule Specification. The release task itself is rather short: the maintainers will tag the repository
and provide the human and machine readable versions of the normative documents.

## Release tasks

This chapter will walk you thru the steps to be taken to

 * prepare a draft - so that the community can work on it
 * release - so that a new version of the spec is created

### prepare a draft

Given the example that the current version of the spec is 0.5.0, collaboration of the specification will continue on the master branch
of https://github.com/projectatomic/nulecule

### release (move from draft to new version)

This will bring the draft version of the spec to a released version of the spec: `git tag v0.6.0 -m 'v0.6.0'` After that, one of the maintainers will
publish the human and machine readable files to http://projectatomic.io/nulecule/spec/0.6.0/

## Maintainers

Please see the MAINTAINERS file for a list of maintainers of the Nulecule Specification.
