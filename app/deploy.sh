#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $REPOSITORY

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker build -t codynators-backend .
deactivate
docker run  -p 5000:443 --name codynators-backend codynators-backend