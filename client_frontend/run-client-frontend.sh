#!/bin/bash
npm run build
docker image build -t client-frontend .
docker run -p 8080:80  client-frontend
