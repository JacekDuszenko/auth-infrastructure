import socket

IP = '127.0.0.1'
PORT = 1313
EXPECTED_HC_RESPONSE = b'alive'
REQUEST = b'deaddead'


# ensure, that auth_service health check is listening on port
def test_health_check():
    s = socket.socket()
    s.connect((IP, PORT))
    s.send(REQUEST)
    assert s.recv(5) == EXPECTED_HC_RESPONSE
    s.send(REQUEST)
    assert s.recv(5) == EXPECTED_HC_RESPONSE
    s.close()

