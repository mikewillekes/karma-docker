FROM java:openjdk-7-jre
MAINTAINER Mike Willekes

WORKDIR /usr/local/lib
RUN mkdir karma
ADD karma.jar /usr/local/lib/karma/

VOLUME /karma
ENV KARMA_USER_HOME=/karma

ENTRYPOINT ["java", "-Xmx4096m", "-cp", "/usr/local/lib/karma/karma.jar"]
CMD ["edu.isi.karma.rdf.OfflineRdfGenerator", "--help"]