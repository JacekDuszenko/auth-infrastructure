import json
import socket
import ssl

from flask import Flask, request
from flask_cors import CORS, cross_origin

MY_PORT = 1313
AUTH_SERVICE_PORT = 8443
AUTH_SERVICE_HOSTNAME = "auth_service"
BUFSIZE = 1024

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


def verify(data: bytes) -> bytes:
    context = ssl._create_unverified_context()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslSock = context.wrap_socket(
        sock, server_side=False, server_hostname=AUTH_SERVICE_HOSTNAME
    )
    sslSock.connect((AUTH_SERVICE_HOSTNAME, AUTH_SERVICE_PORT))
    sslSock.sendall(data)
    resp = sslSock.recv(1024)
    sslSock.close()
    return resp


@app.route("/health_check", methods=["GET"])
def health_check():
    return "OK", 200


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    content = request.get_json(force=True)
    content_str = str(content)
    print("Data received from client is :" + content_str)
    try:
        byteresponse = verify(str.encode(content_str))
        response = byteresponse.decode("utf-8")
        print("Response from auth service is: " + str(response))
        result = json.loads(response).get("authenticated")
        if result == True or result == 'true':
            log_resp(200)
            return response, 200
        else:
            log_resp(401)
            return response, 401
    except socket.timeout:
        log_resp(200)
        return response, 504


def log_resp(rsp_code):
    print("Response code is: ", rsp_code)
    if rsp_code == 200:
        print("Successfully authorized user")
    else:
        print("Failed authorizing user")


if __name__ == "__main__":
    app.run(port=MY_PORT, host="0.0.0.0")
