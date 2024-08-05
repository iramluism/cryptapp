#!/bin/sh
# start.sh

docker compose -f ./deployments/docker-compose.tests.yml build
docker compose -f ./deployments/docker-compose.tests.yml up -d
docker compose -f ./deployments/docker-compose.tests.yml logs run_tests
docker compose -f ./deployments/docker-compose.tests.yml down 