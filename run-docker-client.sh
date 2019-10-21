#!/bin/bash

wget https://github.com/debuerreotype/docker-debian-artifacts/blob/74e1a3304401c2eb9c6624ae1056d0a438c15189/jessie/rootfs.tar.xz
sudo docker build . -t docker-client_backend
sudo docker run docker-client_backend