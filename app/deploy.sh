#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $REPOSITORY

docker stop codynators-backend
docker rm codynators-backend
docker rmi codynators-backend

docker build -t codynators-backend .
docker run -d -p 5000:5000 --name codynators-backend codynators-backend 
