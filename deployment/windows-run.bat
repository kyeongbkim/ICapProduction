@echo off

if [%ICAP_DIR%] == [] goto icap_dir_empty

set CURRENT_DIR=%~dp0
set PYTHONPATH=%ICAP_DIR%

if not exist static (
    mkdir static
    icacls static /grant:r Everyone:f
)

set FLASK_ENV=development
python -m flask run --host=0.0.0.0

exit 0

:icap_dir_empty
    echo Error: ICAP_DIR is empty
    exit 255
