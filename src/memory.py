'''
Created on Jan 21, 2016

@author: QUYEN
'''
import Ceilometer.client as client

_memory_total = 0
_memory_used = 0
_memory = 0
'''
init example
'''
# url = "http://223.194.33.63:5000/v2.0/"
# token = client.get_token(auth_url=url, username="admin", password="pass", tenant_id="592860f0627842de9ce3f81bf701a4ee")
token = client.get_token()
# print token
# cclient = client.get_client(token = token, url="http://223.194.33.63:8777/",)
cclient = client.get_client(token=token)

'''
get data
'''

memory_total = cclient.samples.list('hardware.memory.total', limit=1)
if(len(memory_total) > 0):
    _memory_total = memory_total[0].counter_volume
    
memory_used = cclient.samples.list('hardware.memory.used', limit=1)
if (len(memory_used)>0):
    _memory_used = memory_used[0].counter_volume
    
memory_resident = cclient.samples.list('memory.resident')

for each in memory_resident:
    _memory += each.counter_volume

print "memory_total", _memory_total
print "memory_used", _memory_used
print "memory_amount", _memory
