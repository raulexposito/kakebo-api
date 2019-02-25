#!/bin/bash

echo
echo "======================================================="
echo "ejecución: `date`"
echo "======================================================="
echo

yapf -ir flaskr tests
pylint flaskr/**/*.py --disable=missing-docstring
py.test
