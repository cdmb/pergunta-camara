#!/bin/bash


sudo su - postgres -c psql << EOF
DROP TABLE IF EXISTS pergunta_camara;
DROP TABLE IF EXISTS pergunta_camara_test;
CREATE DATABASE pergunta_camara;
CREATE DATABASE pergunta_camara_test;
CREATE ROLE pergunta WITH LOGIN PASSWORD 'camara';
GRANT ALL PRIVILEGES ON DATABASE pergunta_camara TO pergunta;
GRANT ALL PRIVILEGES ON DATABASE pergunta_camara_test TO pergunta;
EOF
