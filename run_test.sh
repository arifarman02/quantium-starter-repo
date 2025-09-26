#!/bin/bash

. ./venv/bin/activate

python -m pytest test_app.py
exit_code=$?

if [ "$exit_code" -eq 0 ]
then
    exit 0
else
    exit 1
fi