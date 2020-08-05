import re
import urllib.request,urllib.parse,urllib.error
data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/regex_sum_824310.txt").read()
fh = data.decode()
#print(fh)
sum = 0
li = list()
li = (re.findall("[0-9]+",fh))
for num in li:
    sum = sum+int(num)
    #sum = sum + num
#for line in data:
    #print(line)
print(sum)
#print(li)
