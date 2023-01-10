#!/usr/bin/env bash
# Copyright (c) Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

set -e

# Create collection documentation into temporary directory
rm -rf temp-rst
mkdir -p temp-rst
antsibull-docs \
    --config-file antsibull-docs.cfg \
    collection \
    --use-current \
    --dest-dir temp-rst \
    community_fabric.ansible

# Copy collection documentation into source directory
rsync -cprv --delete-after temp-rst/collections/ collections/

# Build Sphinx site
sphinx-build -M html . build -c . -W --keep-going

