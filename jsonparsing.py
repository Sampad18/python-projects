import json
import urllib.request,urllib.parse,urllib.error
html= urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_824315.json').read()
#print(type(html))
fh = html.decode()
info = json.loads(fh)
#print(type(info))
sum = 0
for item in info["comments"]:
    sum = sum+(item["count"])
print(sum)
