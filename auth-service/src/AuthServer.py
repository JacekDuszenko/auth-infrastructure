import socket
import ssl
from pathlib import Path

PORT_NUMBER = 8443
HOSTNAME = '127.0.0.1'
CERT_PATH = Path("../certificates/51787427__127.0.0.1_.cert")
KEY_PATH = Path("../certificates/51787427__127.0.0.1_.key")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERT_PATH, KEY_PATH)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOSTNAME, PORT_NUMBER))
    sock.listen(5)

    with context.wrap_socket(sock, server_side=True) as sslSock:
        while True:
            clientSocket, address = sslSock.accept()
            print("Connection has been established!")

