#!/bin/bash

for unflipped in ${WORKSPACE}/images/*; do
    convert -flip "${unflipped}" "${WORKSPACE}/flipped/$(basename $unflipped)"
done
