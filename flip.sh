#!/bin/bash

for $unflipped in ${WORKSPACE}/images/*; do
    convert -flip "${WORKSPACE}/${unflipped}" "${WORKSPACE}/flipped/$(basename $unflipped)"
done
