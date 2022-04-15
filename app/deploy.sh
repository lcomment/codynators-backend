#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $REPOSITORY

docker build -t codynators-backend .
docker run  -p 443:5000 --name codynators-backend codynators-backend