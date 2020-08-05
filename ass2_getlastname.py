import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
count = 0
li = list()
for i in range(7):
    if i == 0:
        url='  http://py4e-data.dr-chuck.net/known_by_Sylvanna.html'
    fh = urllib.request.urlopen(url)
    soup = BeautifulSoup(fh,'html.parser')
    tags = soup('a')
    for tag in tags:
        if(count==17):
            count=0
            url = tag.get('href')
            li = re.findall('>(.+)<',str(tag))
            #print(li[0])
            break
        else:
            count+=1
            continue

print(li[0])
#print(tag.get('href'))




#    print (li)
