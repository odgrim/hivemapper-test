#!/bin/bash

pushd "${WORKSPACE}/images"
for unflipped in ($@); do
    wget $unfliped
done
popd
