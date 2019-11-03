import json

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from mocks.tls_mock import ssl, socket, SERV_TEMP_RESPONSE

CA_PATH = 0xDEADBEEF
# need to figure it out
MY_PORT = 1313
AUTH_SERVICE_PORT=8443
AUTH_SERVICE_HOSTNAME='auth_service'
BUFSIZE = 1024

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def verify(data: bytes) -> bytes:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CA_PATH)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # 5 seconds
        sock.settimeout(5)
        with context.wrap_socket(sock, server_side=False, do_handshake_on_connect=True) as ssock:
            try:
                ssock.connect((AUTH_SERVICE_HOSTNAME, AUTH_SERVICE_PORT))
                ssock.sendall(data)
                return SERV_TEMP_RESPONSE
            except socket.timeout as timeout:
                raise timeout


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    content = request.json
    content_str = str(content)
    print('data received is:' + content_str)
    try:
        byteresponse = verify(str.encode(content_str))
        response = byteresponse.decode("utf-8")
        print('response is: ' + str(response))
        result = json.loads(response).get("authorisation")
        print(result)
        if result == True:
            log_resp(200)
            return response, 200
        else:
            log_resp(401)
            return response, 401
    except socket.timeout:
        log_resp(200)
        return response, 504

def log_resp(rsp_code):
    print('response code is: ', rsp_code)


if __name__ == '__main__':
    app.run(port=MY_PORT, host='0.0.0.0')
