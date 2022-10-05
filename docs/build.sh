#!/usr/bin/env bash

set -e
cd /Users/agitting/projects/github/ansible-test/ansible_collections/ipfabric/ansible/docs

# Create collection documentation into temporary directory
rm -rf temp-rst
mkdir -p temp-rst
antsibull-docs \
    --config-file antsibull-docs.cfg \
    collection \
    --use-current \
    --dest-dir temp-rst \
    ipfabric.ansible

# Copy collection documentation into source directory
rsync -cprv --delete-after temp-rst/collections/ rst/collections/

# Build Sphinx site
sphinx-build -M html rst build -c . -W --keep-going
