#!/bin/bash

pushd "${WORKSPACE}/images"
for $unflipped in "${params.imgList}"; do
    wget $unfliped
done
popd
