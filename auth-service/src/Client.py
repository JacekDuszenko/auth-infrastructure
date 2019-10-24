# Only for connection testing!!!
import socket
import ssl

PORT_NUMBER = 8443
SERVER_HOSTNAME = '127.0.0.1'

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context = ssl._create_unverified_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslSock = context.wrap_socket(sock, server_side=False, server_hostname=SERVER_HOSTNAME)
sslSock.connect((SERVER_HOSTNAME, PORT_NUMBER))
print("Client started")
sslSock.close()
