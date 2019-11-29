import requests
import subprocess


BACKEND_ENDPOINT = 'http://client_backend:1313/health_check'
LDAP_PORT = 636
AUTH_ENDPOINT = "http://auth_service:1313/health_check"


def test_client_backend_hc():
    assert requests.get(BACKEND_ENDPOINT).status_code == 200

def test_ldap_hc():
    assert subprocess.call("ldap-health-check.sh", shell=True) == LDAP_PORT

def test_auth_service_hc():
    assert requests.get(AUTH_ENDPOINT).status_code == 200
