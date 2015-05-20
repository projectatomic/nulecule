# Lifecycle of the Specification

This document and the processes it describes will become effective starting Nulecule Specification 0.5.0. It is valid until replaced by a newer version or noted otherwise.

## Normative Document

The normative Nulecule Specification document will be published at http://www.projectatomic.io/nulecule/spec/<major.minor.patch>/index.html
Versioning is using the [semantic versioning scheme](http://semver.org/spec/v2.0.0.html).

For convenience the latest version of the specification will be located at http://www.projectatomic.io/nulecule/spec/latest/index.html and redirect to the corresponding versioned URL.
All versions of the specification will be available using their corresponding URL.

## States

The Nulecule Specification will have a certain set of releases, we will use semantic versioning to identify the releases. 
Prior each release there will be a draft version of the release. This will be use to work/collaborate on the spec itself.

## Contributors and release process

Everybody is welcome to contribute to the draft version of the upcoming release. This will be documented by pull 
requests to the draft of the specification. Once a draft has stabilized, it will be prepared by the specification 
maintenance team and prepared for release. The maintainers will release a new release of the specification.

### Changes to a Releases

Changes to released versions of the specification will not change the structure or feature set of the specification. 
They are only meant to fix spelling or language errors, add or correct examples.

## Release tasks

This chapter will walk you thru the steps to be taken to 

 * prepare a draft - so that the community can work on it
 * release - so that a new version of the spec is created

### prepare a draft

Given the example that the current version of the spec is 0.5.0, you do the following:
```
git branch 0.6.0-draft
git checkout 0.6.0-draft
cd spec
mkdir 0.6.0
cp -r 0.5.0/* 0.6.0/
git add 0.6.0
cd 0.6.0 && vi <somestuff>
```

### release (move from draft to new version)

This will bring the draft version of the spec to a released version of the spec

```
git checkout master
git merge 0.6.0-draft
git tag 0.6.0 -m '0.6.0'
```

## Maintainers

Please see the MAINTAINERS file for a list of maintainers of the Nulecule Specification.

