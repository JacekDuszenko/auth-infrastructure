import socket
import ssl
from pathlib import Path
import os
import json
import docker
import subprocess

from ldap3 import Server, Connection, ALL, Tls, KERBEROS


SERVER_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PORT_NUMBER = 8443
HOSTNAME = '127.0.0.1'
CERT_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.cert")
KEY_PATH = Path(f"{SERVER_DIRECTORY}/../certificates/51787427__127.0.0.1_.key")


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(CERT_PATH, KEY_PATH)




def ldap_auth():
    
    cmd = ['docker', 'inspect','--format=\'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}\'', 'teamprogramming2k19_ldap-host_1']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()
    IP=o.decode('ascii').replace("'", "")
  

    #binddn = "cn=admin,dc=group-project,dc=com"
    #pw = "admin"

   # server = Server(host=IP, get_info=ALL, tls=Tls(ca_certs_file='default-ca.pem',local_certificate_file='ldap.crt', local_private_key_file='51787427__127.0.0.1_.cert', validate=ssl.CERT_REQUIRED))
    server = Server(host=IP, get_info=ALL)
    conn = Connection(server)
   # conn.open()
   # conn.start_tls()
    conn.bind()
   # print(conn)
    if conn.bind():
        print('\nSuccesfully connected to ldap \n',server.info)
        conn.unbind()
        return True
    return False
    

def run_server():
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

         
                    if ldap_auth():
                        response = json.dumps({"authenticated": "true"})					
                    else:
                        response = json.dumps({"authenticated": "false"})

                    sslSock.sendall(str.encode(response))

                except ssl.SSLError as e :
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


if __name__ == '__main__':
    run_server()
