#!/bin/bash
pushd client
npm install
npm run build
popd
pushd server
source myprojectenv/bin/activate
./bootstrap.sh
