import json

from flask import Flask, request

from mocks.tls_mock import ssl, socket, SERV_TEMP_RESPONSE

SERVER_HOSTNAME = 0xDABBAD00
CA_PATH = 0xDEADBEEF
CLIENT_PORT = 1313
# need to figure it out
SERVER_PORT = 2525
BACKEND_HOST = 8080
BUFSIZE = 1024

app = Flask(__name__)


def verify(data: bytes) -> bytes:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CA_PATH)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 5 seconds
        sock.settimeout(5)
        with context.wrap_socket(sock, server_side=False, do_handshake_on_connect=True) as ssock:
            try:
                ssock.connect((SERVER_HOSTNAME, SERVER_PORT))
                ssock.sendall(data)
                return SERV_TEMP_RESPONSE
            except socket.timeout as timeout:
                raise timeout


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = request.form['nm']
    pswd = request.form['pw']
    data = json.dumps({"email": user, "password": pswd})
    try:
        byteresponse = verify(str.encode(data))
        response = byteresponse.decode("utf-8")
        result = json.loads(response).get("authorisation")
        if result == "True":
            return "OK", 200
        else:
            return "Unauthorized", 401
    except socket.timeout:
        return "Gateway Timeout", 504


if __name__ == '__main__':
    app.run()
