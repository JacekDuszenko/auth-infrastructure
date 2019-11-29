import unittest


class Test_auth_service_methods(unittest.TestCase):

    def test_validation_test(self):
        client = Client
        email = "user@domain.com"
        password = "password"
        self.assertEqual(client.connect(client, email, password), b'{"authenticated": "true"}')

    def test_invalid_credentials(self):
        client = Client
        email = "invalid_mail@domain.com"
        password = "invalid_password"
        self.assertNotEqual(client.connect(client, email, password), b'{"authenticated": "true"}')


if __name__ == '__main__':
    unittest.main()
