import xml.etree.ElementTree as et
import urllib.request,urllib.parse,urllib.error
#from bs4 import BeautifulSoup
import re
url = 'http://py4e-data.dr-chuck.net/comments_824314.xml'
xml = urllib.request.urlopen(url).read()
#s = BeautifulSoup(xml,'html.parser')
#print(s)
tree = et.fromstring(xml)
sum = 0
#st = list()
counts = tree.findall('.//comment')
for item in counts:
    sum = sum +int(item.find('count').text)
print(sum)


#count = (tree.findall('.//count'))
#print(count)
#print(type(count))
#for item in count:
#    print(item.find('count').text)
