#!/bin/bash

if [ -z "${GITLAB_USERNAME}" ]; then
    echo "set GITLAB_USERNAME environment variable"
    exit 1
fi
echo "Enter your gitlab password"
docker login registry.gitlab.com --username $GITLAB_USERNAME

docker-compose up -d

cd integ-test
docker image build -t integ-test .
docker run -d integ-test
cd ../

docker rm $(docker stop $(docker ps -a -q --filter ancestor=integ-test --format="{{.ID}}"))
docker-compose down


