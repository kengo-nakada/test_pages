#!/usr/bin/env bash

set -e

echo "Cleaning old build..."
rm -rf _build

echo "Building Sphinx..."
sphinx-build -b html . _build/html

echo "Build finished."
echo "Open _build/html/index.html"