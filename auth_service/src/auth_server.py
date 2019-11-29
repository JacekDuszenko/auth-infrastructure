import json
import socket
import ssl
import threading

from config import (
    PORT_NUMBER,
    HOSTNAME,
    CERT_PATH,
    KEY_PATH
)
from flask import Flask
from ldap_con import authorize

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERT_PATH, KEY_PATH)


def ldap_auth(email, password):
    is_authorized = authorize(email, password)
    if is_authorized:
        print('\nSuccesfully authorized user with email {} and password {} in ldap\n'.format(email, password))
    else:
        print('\nFailed authorizing user with email {} and password {} in ldap\n'.format(email, password))

    return is_authorized


def listen_client():
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
                    sslSock.verify_mode = ssl.CERT_NONE
                    print("TLS connection has been established!")

                    clientRequest = sslSock.recv(1024)
                    jsonRequest = json.loads(clientRequest.decode("utf-8").replace("\'", "\""))
                    email = jsonRequest["email"]
                    password = jsonRequest["password"]

                    if ldap_auth(email, password):
                        response = json.dumps({"authenticated": "true"})
                    else:
                        response = json.dumps({"authenticated": "false"})

                    sslSock.sendall(str.encode(response))

                except ssl.SSLError as e:
                    print("TLS Handshake failed!")
                    print(e)
                    continue
                finally:
                    sslSock.shutdown(socket.SHUT_RDWR)
                    sslSock.close()
                    print("Connection closed!")

            except socket.error as a:
                print(a)
                print("Socket connection failed! OSError!")


@app.route("/health_check", methods=["GET"])
def health_check():
    return "OK", 200


def run_hc():
    app.run(port=1313, host="0.0.0.0")


if __name__ == "__main__":
    auth = threading.Thread(target=listen_client)
    auth.start()
    hc = threading.Thread(target=run_hc)
    hc.start()
