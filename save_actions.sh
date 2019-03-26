#!/bin/bash

echo
echo "======================================================="
echo "ejecución: `date`"
echo "======================================================="
echo

find flaskr/ tests/ -type d -name "__pycache__" -exec rm -rf {} \;
flake8 flaskr tests
py.test
