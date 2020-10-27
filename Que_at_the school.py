from pip._vendor.distlib.compat import raw_input
import re
n,t=map(int,raw_input().split())
s=str(raw_input())
i=0
while i<t:
    x=re.sub("BG","GB",s)
    s=x
    i+=1
print(x)
