#!/usr/bin/env bash

docker build -t "karma/offline" ./karma-offline
docker build -t "karma/web" ./karma-web

