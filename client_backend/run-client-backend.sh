#!/bin/bash
 docker build --no-cache . -t docker-client
 docker run -d docker-client
