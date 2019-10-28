import socket
import ssl
import json
import docker
import subprocess

from ldap3 import Server, Connection, ALL, Tls, KERBEROS

from threading import Thread
from config import(
    SERVER_DIRECTORY,
    PORT_NUMBER,
    HOSTNAME,
    CERT_PATH,
    KEY_PATH,
    HEALTH_CHECK_PORT,
    HEALTH_CHECK_BUFSIZE
)


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


def listen_health_check():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', HEALTH_CHECK_PORT))
        s.listen(1)
        c, addr = s.accept()
        while True:
            c.recv(HEALTH_CHECK_BUFSIZE)
            c.send(b'alive')

if __name__ == '__main__':
    Thread(target=listen_client()).start()
    Thread(target=listen_health_check()).start()
    run_server()


