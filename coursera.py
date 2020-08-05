import re
x="From stphen.msrqud@uy.54.yt 07 09.8.9"
y=re.findall('^From \S+[0-9]\S.+([0-9]+)\s+?', x)
print(y)
