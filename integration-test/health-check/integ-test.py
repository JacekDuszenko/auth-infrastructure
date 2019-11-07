import requests

BACKEND_ENDPOINT = 'http://client_backend:1313/health_check'


def test_client_backend_hc():
    assert requests.get(BACKEND_ENDPOINT).status_code == 200
