#!/bin/bash

for f in book*
do
    a="$(echo $f | sed s/^book/algorithm-ebook/)"
    mv "$f" "$a"
done
