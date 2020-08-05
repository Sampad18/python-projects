import urllib.request,urllib.parse,urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
surl = 'http://py4e-data.dr-chuck.net/json?'
para = dict()
para['address']="RPI"
para['key']=42
url = surl + urllib.parse.urlencode(para)
#print(url)
data = urllib.request.urlopen(url, context=ctx).read()
ch = data.decode()
fh = json.loads(ch)
#print(fh)
for item in fh["results"]:
    print(item["place_id"])
#tree = et.fromstring(data)
#print(data.decode())
#data = fh.read()
