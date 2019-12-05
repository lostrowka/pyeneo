#!/bin/bash
apt-get update && apt-get upgrade -y  
apt-get install python3.7 -y
apt-get install git-all -y
mkdir io
cd io
git clone https://github.com/lostrowka/pyeneo.git
apt-get install python3-venv
python3.7 -m venv my_env
source my_env/bin/activate
cd pyeneo
python -m pip -r requirements.txt
export PYTHONPATH=$(pwd)
python server/website manage.py runserver
