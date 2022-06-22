#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2/flask/app

cd $REPOSITORY
sudo apt-get install libgl1-mesa-glx

docker stop codynators-backend
docker rm codynators-backend
docker rmi codynators-backend

docker build -t codynators-backend .
docker run -d -p 443:5000 --name codynators-backend codynators-backend 
