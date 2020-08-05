import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
#url = input('enter file name-')
fh = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_824312.html')
soup= BeautifulSoup(fh,'html.parser')
tags = soup('span')
sum = 0
li=[]
for tag in tags:
    li=(re.findall('>(.+)<',str(tag)))
    sum = sum+int(li[0])
print(sum)
    #print(li)
