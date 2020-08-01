#!/bin/bash

pushd "${WORKSPACE}/images"

for unflipped in $(echo "$@"); do
    wget $unflipped
done
popd
