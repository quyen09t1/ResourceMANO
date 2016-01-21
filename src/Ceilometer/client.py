'''
Created on Jan 20, 2016

@author: QUYEN
'''
from keystoneclient.auth.identity import v2
from keystoneclient import session
from ceilometerclient import client

_os_username = "admin"
_os_password = "secrete"
_auth_url = "http://116.89.184.80:5000/v2.0/"
_url = "http://116.89.184.80:8777"
_os_tenant_name = "admin"
_os_tenant_id = "a82945a77c64448591ebc3ac517284fc"

def get_token(auth_url = _auth_url, username = _os_username, password = _os_password, tenant_id = _os_tenant_id):
    auth = v2.Password(auth_url = auth_url, username = username, password = password, tenant_id = tenant_id)
    sess = session.Session(auth = auth, verify = False)
    token = auth.get_token(sess)
    return token

def get_client(token, url = _url, verify = False):
    ceilometer_client = client.get_client(2, ceilometer_url = url, token = token, verify = verify)
    return ceilometer_client

#token = get_token()
#print token

#get_client(token = token)

#print "oke"