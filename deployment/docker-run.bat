@echo off

if [%ICAP_DIR%] == [] goto icap_dir_empty

set CURRENT_DIR=%~dp0

if not exist static (
    mkdir static
    icacls static /grant:r Everyone:f
)

docker run -it --rm ^
    -p 5000:5000 ^
    -v %CURRENT_DIR%:/flask ^
    -v %ICAP_DIR%:/icap ^
    --env FLASK_ENV=development ^
    --env PYTHONPATH=/icap ^
    --name flask ^
    flask
exit 0

:icap_dir_empty
    echo Error: ICAP_DIR is empty
    exit 255
