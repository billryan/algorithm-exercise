#!/bin/bash

git ls-tree -r --name-only HEAD | while read filename; do
  echo "$(git log -1 --format="%ad" --date=short -- $filename) $filename"
done
