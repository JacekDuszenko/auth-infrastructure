#!/bin/bash
npm run build
docker image build -t client-frontend .
docker run -p 4200:80 -d --rm client-frontend
