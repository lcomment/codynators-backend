#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $DIR

if [ -n "$XDG_RUNTIME_DIR" ]
then
   echo "opening browser with xdg-open"
   sleep 2
   xdg-open "https://localhost:8443/fig-flask-basic"
else
   echo "available on https://localhost:8443/fig-flask-basic"
fi

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker build -t codynators-backend .
deactivate
docker run  -p 5000:443 --name codynators-backend codynators-backend