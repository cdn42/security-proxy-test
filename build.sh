#!/usr/bin/env bash

if (which docker) ; then
    echo "-- [OK]: Docker Installed"

    echo "- Building Docker Image"
    docker build --tag cdn42/security-proxy-test .
    echo "- Running Docker Image"
    docker run -d -p 9000:9000 --name security-proxy-test cdn42/security-proxy-test:latest

else

    echo "-- [ERROR]: Can't find Docker"
    exit

fi
