#!/bin/bash

echo
echo "======================================================="
echo "ejecución: `date`"
echo "======================================================="
echo

yapf -ir flaskr tests
flake8 flaskr tests
py.test
