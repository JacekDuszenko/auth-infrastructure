#!/bin/bash
docker ps -f "status=running" -f "name=ldap-host" | grep -o 636