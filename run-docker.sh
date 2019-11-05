docker-compose pull
docker-compose up -d 

sleep 2

PHPLDAP_IP=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'  teamprogramming2k19_ldap-admin_1)

echo "Go to: http://$PHPLDAP_IP"
echo "Login DN: cn=admin,dc=group-project,dc=com"
echo "Password: admin"

ADMIN_ID=$(docker inspect -f '{{.Config.Hostname}}'  teamprogramming2k19_ldap-admin_1)
LDAP_ID=$(docker inspect -f '{{.Config.Hostname}}'  teamprogramming2k19_ldap-host_1)

mkdir -p ./ldap
docker cp $LDAP_ID:/container/service/slapd/assets/certs ./ldap/ldap-certs
docker cp $LDAP_ID:/container/service/:ssl-tools/assets/default-ca/ ./ldap/ldap-certs/default-ca
docker cp $ADMIN_ID:/container/service/phpldapadmin/assets/apache2/certs ./ldap/phpadmin-certs
