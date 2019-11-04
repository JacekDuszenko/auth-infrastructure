#!/bin/bash -e
#
# Do not use unless you want to test LDAP component separately
#
LDAP_CID=$(docker run --name ldap_service --hostname ldap-service --env LDAP_ORGANISATION="project" --env LDAP_DOMAIN="project.com" --env LDAP_ADMIN_PASSWORD="project" --detach osixia/openldap:1.3.0)
PHPADMIN_CID=$(docker run --name phpldapadmin_service --hostname phpldapadmin_service --link ldap-service:ldap-host --env PHPLDAPADMIN_LDAP_HOSTS=ldap-host --detach osixia/phpldapadmin:0.9.0)

PHPLDAP_IP=$(docker inspect -f "{{ .NetworkSettings.IPAddress }}" phpldapadmin_service)

echo "Go to: https://$PHPLDAP_IP"
echo "Login DN: cn=admin,dc=project,dc=com"
echo "Password: project"

sleep 2

# extract certificates from both images
docker cp $LDAP_CID:/container/service/slapd/assets/certs ./ldap-certs
docker cp $PHPADMIN_CID:/container/service/phpldapadmin/assets/apache2/certs ./phpadmin-certs
