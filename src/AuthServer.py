import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl
from pathlib import Path

PORT_NUMBER = 8443
HOSTNAME = '127.0.0.1'
CERT_PATH = Path("../certificates/51787427__127.0.0.1_.cert")
KEY_PATH = Path("../certificates/51787427__127.0.0.1_.key")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(CERT_PATH, KEY_PATH)

sock = socket.socket() 
sock.bind((HOSTNAME, PORT_NUMBER))
sock.listen(5)
while True:
    clientSocket, address = sock.accept()
    sslSock = context.wrap_socket(clientSocket, server_side=True)
    print("Connection has been established!")
    buf = ''  # Buffer to hold received client data
    try:
                #polecenia od klienta
                print("Received:", buf)
                break
    finally:
        print("CLOSING")
        sslSock.shutdown(socket.SHUT_RDWR)
        sslSock.close()

