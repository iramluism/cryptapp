#!/bin/sh

docker compose -f ./deployments/docker-compose.tests.yml build
docker compose -f ./deployments/docker-compose.tests.yml up -d --abort-on-container-exit
docker compose -f ./deployments/docker-compose.tests.yml logs run_tests
