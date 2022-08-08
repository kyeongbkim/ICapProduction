#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate python-3.9.12

python -m pip install --upgrade pip
pip install -r '/tmp/requirements.txt'
