#!/bin/sh
wget https://raw.githubusercontent.com/luminoso/fedora-copr-vorta/main/vorta.spec

# update directly from release tags
VERSION=$(git ls-remote --refs --sort="version:refname" --tags https://github.com/borgbase/vorta.git | cut -d/ -f3-|tail -n1|cut -d'v' -f2)

echo "Version to build: ${VERSION}"
sed -i "s/Version:        .*/Version:        ${VERSION}/g" vorta.spec
