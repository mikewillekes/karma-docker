#!/usr/bin/env bash
docker run -v /karma:/karma -v /data:/data karma/offline \
           edu.isi.karma.rdf.OfflineRdfGenerator \
           --sourcetype CSV \
           --filepath /data/data-ebola-public-sample.csv \
           --modelfilepath /data/data-ebola-public-model.ttl \
           --root http://isi.edu/dig/ontology/ebola/EbolaEvent1 \
           --sourcename "Ebola Case Data" \
           --outputfile /data/output.n3 \
           --jsonoutputfile /data/output.json
