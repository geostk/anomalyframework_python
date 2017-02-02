# Python implementation of the Anomaly Detection Framework
A cleaner implementation of the Del Giorno, Bagnell, Hebert ECCV 2016 paper 'A Discriminative Framework for Anomaly 
Detection in Large Videos'

## Installation
== Run: 

sh install.sh

A successful build will run the tests and say 'OK' at the end.

If the installation succeeds but the tests fail, check whether there are any missing python packages (e.g. - pip install sklearn)

## Build
Rather than cluttering the source directory with build files, run the following:
cmake -Bbuild -H.; cd build/; make; cd ../

This will create a build in the build/ folder.