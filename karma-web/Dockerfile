FROM tomcat:7-jre7
MAINTAINER Mike Willekes

ADD karma.war /usr/local/tomcat/webapps/
ADD setenv.sh /usr/local/tomcat/bin/

VOLUME /karma
ENV KARMA_USER_HOME=/karma

CMD ["catalina.sh", "run"]
