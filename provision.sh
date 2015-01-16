#!/usr/bin/env bash

# Get prerequisites
sudo apt-get -y update
sudo apt-get install -y -q curl git openjdk-7-jdk maven

# Get Karma sources
git clone https://github.com/usc-isi-i2/Web-Karma.git /webkarma
cd /webkarma && git checkout development

# Build Karma
cd /webkarma && mvn clean install
cd /webkarma/karma-offline && mvn assembly:assembly -DdescriptorId=jar-with-dependencies

# Copy artifacts for Docker build
cp /webkarma/karma-web/target/karma-web-0.0.1-SNAPSHOT.war /vagrant/karma-web/karma.war
cp /webkarma/karma-offline/target/karma-offline-0.0.1-SNAPSHOT-jar-with-dependencies.jar /vagrant/karma-offline/karma.jar
