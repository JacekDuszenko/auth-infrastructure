# Only for connection testing!!!
import socket
import ssl
import json
import unittest


class Client:
    def connect(self,email, password):
        PORT_NUMBER = 8443
        SERVER_HOSTNAME = '127.0.0.1'

        # context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context = ssl._create_unverified_context()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sslSock = context.wrap_socket(sock, server_side=False, server_hostname=SERVER_HOSTNAME)
        sslSock.connect((SERVER_HOSTNAME, PORT_NUMBER))
        print("Client started")
        data = json.dumps({"email": email, "password": password})
        sslSock.sendall(str.encode(data))
        print(sslSock.recv(1024))
        sslSock.close()


if __name__ == '__main__':
    email = "user@domain.com"
    password = "password"
    client = Client
    client.connect(client,email, password)


