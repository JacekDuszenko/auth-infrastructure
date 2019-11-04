#!/bin/bash
NETWORK='teamprogramming2k19_integ-test'
INTEG_TEST_APP='integ-test-app'

if [ -z "${GITLAB_USERNAME}" ]; then
    echo "set GITLAB_USERNAME environment variable"
    exit 1
fi
echo "Enter your gitlab password"
docker login registry.gitlab.com --username $GITLAB_USERNAME

docker image build -t ${INTEG_TEST_APP} integ-test/ #buduje obraz aplikacji integ-test

docker-compose up -d  #uruchamia system kontenerów

docker run -d ${INTEG_TEST_APP} #uruchamia kontener integ-test
INTEG_TEST_CONTAINER=$(docker ps -a -q --filter ancestor=${INTEG_TEST_APP} --format="{{.ID}}")  #Znajduje ID kontenera na podstawie nazwy image'a
docker network connect "${NETWORK}" "${INTEG_TEST_CONTAINER}"  #Dołącza kontener z aplikacją integ-test do networka, w którym są pozostałe aplikacje

docker rm $(docker stop ${INTEG_TEST_CONTAINER})  #usuwa kontener integ-test
docker-compose down #usuwa wszystkie kontenery aplikacji
