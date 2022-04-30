#!/bin/bash

ALPHANET_NAME="liberty"
TESTS_DIRECTORY="tests/"
TESTS_REPORTS_DIRECTORY="tests/reports"
python -m pytest -v ${TESTS_DIRECTORY}/run_tests.py --network ${ALPHANET_NAME} --junitxml="${TESTS_REPORTS_DIRECTORY}/xunit.xml"