# Only for connection testing!!!

import socket
import ssl

PORT_NUMBER = 8443
SERVER_HOSTNAME = '127.0.0.1'

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context = ssl._create_unverified_context()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_HOSTNAME) as sslSock:
        sslSock.connect((SERVER_HOSTNAME, PORT_NUMBER))
