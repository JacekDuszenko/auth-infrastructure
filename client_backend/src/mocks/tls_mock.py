from unittest.mock import MagicMock

# remove when server will be up
SERV_TEMP_RESPONSE = b'{"authorisation": true}'

class ssl:
    """mock class for better encapsulation"""
    PROTOCOL_TLS_CLIENT = 0xDEADDEAD
    PROTOCOL_TLS_SERVER = 0xDEADFEED

    @staticmethod
    def SSLContext(foo):
        return MagicMock()


class socket:
    """mock class for better encapsulation"""
    AF_INET = 0xDEADDEAD
    SOCK_STREAM = 0xDEADFEED

    @staticmethod
    def socket(foo, bar):
        return MagicMock()

    class timeout(Exception):
        pass
