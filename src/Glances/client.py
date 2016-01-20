'''
Created on Jan 20, 2016

@author: QUYEN
'''
import xmlrpclib
#import json

_url = ""

def set_url(url):
    _url = url 

def connect_server():
    server = xmlrpclib.ServerProxy(_url)
    return server

#print s.getAll()

#print s.getCpu()

#d = json.loads(s.getMem())

#print d['available']