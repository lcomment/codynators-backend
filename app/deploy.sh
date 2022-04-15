#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $REPOSITORY

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker build -t codynators-backend .
docker run  -p 443:5000 --name codynators-backend codynators-backend