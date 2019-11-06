import requests

assert requests.get('http://client_backend:1313').status_code == 200
