'''
Created on Jan 26, 2016

@author: QUYEN
'''
import Ceilometer.client as client

_disk_size_total = 0
_disk_size_used = 0

'''
init example
'''

token = client.get_token()
cclient = client.get_client(token=token)

'''
get data
'''

disk_size_total = cclient.samples.list('hardware.disk.size.total', limit=1)
if(len(disk_size_total) > 0):
    _disk_size_total = disk_size_total[0].counter_volume
    
disk_size_used = cclient.samples.list('hardware.disk.size.used', limit=1)
if (len(disk_size_used)>0):
    _disk_size_used = disk_size_used[0].counter_volume
    
print "disk_size_total", _disk_size_total
print "disk_size_used", _disk_size_used

