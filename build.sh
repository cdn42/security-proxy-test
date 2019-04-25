#!/usr/bin/env bash
echo
echo          _       _  _  ____               _
echo   ___ __| |_ __ | || ||___ \   _ __   ___| |_
echo  / __/ _` | '_ \| || |_ __) | | '_ \ / _ \ __|
echo | (_| (_| | | | |__   _/ __/ _| | | |  __/ |_
echo  \___\__,_|_| |_|  |_||_____(_)_| |_|\___|\__|
echo
echo

if [ `which docker` ]; then
    echo "-- [OK]: Docker Installed"

    echo "- Building Docker Image"
    docker build --tag cdn42/security-proxy-test .
    echo "- Running Docker Image"
    docker run -d -p 9000:9000 --name security-proxy-test cdn42/security-proxy-test:latest

else

    echo "-- [ERROR]: Can't find Docker"
    exit

fi