import os
from pathlib import Path

SERVER_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PORT_NUMBER = 8443
HOSTNAME = "0.0.0.0"
CERT_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.cert")
KEY_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.key")
HEALTH_CHECK_PORT = 1313
HEALTH_CHECK_BUFSIZE = 8
LDAP_HOST="ldap-host"
