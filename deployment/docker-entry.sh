#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate python-3.9.12

python -m flask run --host=0.0.0.0
