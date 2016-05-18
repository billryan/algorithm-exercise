#!/bin/bash

for old_file in book*
do
    new_file="$(echo ${old_file} | sed s/^book/algorithm-ebook/)"
    mv "${old_file}" "${new_file}"
done
