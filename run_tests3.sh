#!/usr/bin/env bash

set -eux

# prepare python environment
VENV_PATH="/tmp/testgres_venv"
rm -rf $VENV_PATH
python -m venv "${VENV_PATH}"
export VIRTUAL_ENV_DISABLE_PROMPT=1
source "${VENV_PATH}/bin/activate"
pip install -r tests/requirements.txt

# install testgres' dependencies
export PYTHONPATH=$(pwd)

# Check codestyle
flake8 .

# Run builtin tests
python3 -m pytest -l -vvv tests

set +eux
