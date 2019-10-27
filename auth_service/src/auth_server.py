import socket
import ssl
from pathlib import Path
import os
import json

SERVER_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PORT_NUMBER = 8443
HOSTNAME = '127.0.0.1'
CERT_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.cert")
KEY_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.key")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(CERT_PATH, KEY_PATH)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOSTNAME, PORT_NUMBER))
    sock.listen(5)
    while True:
        print("Waiting for client connection...")

        try:
            clientSocket, address = sock.accept()
            print("Socket connection has been established!")

            try:
                sslSock = context.wrap_socket(clientSocket, server_side=True)
                print("TLS connection has been established!")

                clientRequest = sslSock.recv(1024)
                jsonRequest = json.loads(clientRequest.decode("utf-8"))
                email = jsonRequest["email"]
                password = jsonRequest["password"]

                if email == "user@domain.com" and password == "password":
                    response = json.dumps({"authenticated": "true"})
                else:
                    response = json.dumps({"authenticated": "false"})
                sslSock.sendall(str.encode(response))

            except ssl.SSLError:
                print("TLS Handshake failed!")
                continue
            finally:
                sslSock.shutdown(socket.SHUT_RDWR)
                sslSock.close()
                print("Connection closed!")

        except socket.error as a:
            print(a)
            print("Socket connection failed! OSError!")
