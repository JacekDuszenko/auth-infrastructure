##How to run:

#To run locally
1. Write in command line 'sudo ./run-client-frontend.sh'
2. The script will build the project, build a docker image of recently built project and create and run docker container.
3. To reach your application open the browser on localhost:4200
4. If in doubt, contact Arek Bochenek or Marcin Umiński

## To build image and push it to registry set GITLAB_USERNAME and GITLAB_PASSWORD environment variables with your gitlab credentials and then issue
*./build-client-frontend.sh*