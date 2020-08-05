import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Game"
html = urllib.request.urlopen(url).read()
s = BeautifulSoup(html,"html.parser")
tags = s('a')
dd= dict()

for t in tags:
    print(t.get('href',None))
    #dd[t] = dd.get(t,0)+1
#d =dict([(y,x) for x,y in dd.items()])
#print(d)
#print(dd)

#    print(x[0],x[1])
