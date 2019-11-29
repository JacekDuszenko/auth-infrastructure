import unittest


class Test_auth_service_methods(unittest.TestCase):


    #before running tests run AuthServer.py
    def test_validation_test(self):
        client = Client
        email = "user@domain.com"
        password = "password"
        self.assertEqual(client.connect(client, email, password), b'{"authenticated": "true"}')
        # should be b'{"authenticated": "true"}'


    def test_invalid_credentials(self):
        client = Client
        email = "invalid_mail@domain.com"
        password = "invalid_password"
        self.assertNotEqual(client.connect(client, email, password), b'{"authenticated": "true"}')
        # should be b'{"authenticated": "false"}'

if __name__ == '__main__':
    unittest.main()
