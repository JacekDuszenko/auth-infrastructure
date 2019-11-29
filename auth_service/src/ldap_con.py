from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPBindError as Authorization_Failed
from config import LDAP_HOST

def authorize(email, password) -> bool:
    username, domain = email.split("@")
    domain = domain.replace(".com", "")
    domain = domain.replace(".pl", "")
    login_data = "cn=" + username + ",cn=" + domain + ",dc=group-project," + "dc=com"
    server = Server(host=LDAP_HOST, get_info=ALL)
    try:
        conn = Connection(server, login_data, password, auto_bind=True)
        return True
    except Authorization_Failed:
        return False