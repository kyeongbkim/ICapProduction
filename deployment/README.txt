* Run on Windows
pip install -r requirements.txt
$Env:ICAP_DIR = "C:\ICapProduction\icap"
windows-run.bat

* Run on Docker environment
docker build -t flask .
$Env:ICAP_DIR = "C:\ICapProduction\icap
docker-run.bat
