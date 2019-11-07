#!/bin/bash
INTEG_TEST_APP='integ-test-app'
CLIENT_BACKEND_APP='registry.gitlab.com/jacekduszenko/teamprogramming2k19/client_backend:latest'

if [ -z "$(docker-compose ps -q client_backend)" ]; then    #Sprawdzenie czy działa kontener client_backend, czyli czy został odpalony docker-compose
    echo "Unable to perform integration test. Run docker-compose first."
    exit 1
fi
if [ -z "${GITLAB_USERNAME}" ]; then
    echo "set GITLAB_USERNAME environment variable"
    exit 1
fi
echo "Enter your gitlab password"
docker login registry.gitlab.com --username $GITLAB_USERNAME

docker image build -t ${INTEG_TEST_APP} integration-test/health-check  #buduje obraz aplikacji integ-test

CLIENT_BACKEND_CONTAINER_ID=$(docker ps -a -q --filter ancestor=${CLIENT_BACKEND_APP} --format="{{.ID}}") #pobiera id kontenera client_backend
NETWORK_NAME=$(docker inspect "${CLIENT_BACKEND_CONTAINER_ID}" --format='{{range $k,$v := .NetworkSettings.Networks}}{{$k}}{{end}}') #pobiera nazwę networka, w którym znajduje się client_backend

echo 'Network name: ' ${NETWORK_NAME}
docker run --network=${NETWORK_NAME} -d ${INTEG_TEST_APP} #uruchamia kontener integ-test
INTEG_TEST_CONTAINER_ID=$(docker ps -a -q --filter ancestor=${INTEG_TEST_APP} --format="{{.ID}}")  #Znajduje ID kontenera na podstawie nazwy image'a

# docker rm $(docker stop ${INTEG_TEST_CONTAINER_ID})  #usuwa kontener integ-test
