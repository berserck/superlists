#!/bin/bash
# Script Name:run_tests.sh
# Description: Script to run the tests
#
# Coded by <pedro.parracho@cern.ch>
#
echo "========================"
echo "Running functional tests"
echo "========================"
python3 functional_tests.py
echo -e "\n\n========================"
echo "Running unit tests"
echo "========================"
python3 manage.py test