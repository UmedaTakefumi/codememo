#!/bin/bash

DOCKER_TAG="ss-$(pwd | awk -F/ '{ print $NF }')"

function build () {
  docker build -t $DOCKER_TAG .
}

function login () {
  docker run -it $DOCKER_TAG /bin/bash
}

function root_login () {
  docker exec -it --user root $DOCKER_TAG /bin/bash
}

if [ $1 = "build"  ]; then
  build
elif [ $1 = "login" ]; then
  login
elif [ $1 = "root_login" ]; then
  root_login	
fi

