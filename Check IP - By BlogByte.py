import re
import json
import urllib.request
import socket

localhost = socket.gethostname()
localIP = socket.gethostbyname(localhost)

print('-------------------------------')
print('___Check My IP - By BlogByte___')
print('-------------------------------\n')

print('--------------------')
print('__Your Local IP__')
print('--------------------\n')

print('LocalHot : ', localhost)
print('LocalIP : ', localIP ,'\n')

url = 'http://ipinfo.io/json'
response = urllib.request.urlopen(url)
data = json.load(response)
IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('--------------------')
print('__Your Remote IP__')
print('--------------------\n')
print( 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nHost : {0}'.format(org,region,country,city,IP))
