import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    servicecurl = 'https://py4e-data.dr-chuck.net/json?'

else:
    servicecurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter Location: ")
    if len(address) < 1:break

    params = dict()
    params['address'] = address
    if api_key is not False:  params['key'] = api_key
    


