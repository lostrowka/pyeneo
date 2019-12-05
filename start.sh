#!/bin/bash
apt-get update && apt-get upgrade -y
apt-get install python3.7 -y
apt-get install git-all -y
apt-get install pipenv -y
mkdir io
cd io
git clone https://github.com/lostrowka/pyeneo.git
python3.7 -m pip install venv
python3.7 -m venv my_env
source my_env/bin/activate
python -m pip -r
cd pyeneo
export PYTHONPATH=$(pwd)
python server/website manage.py runserver
