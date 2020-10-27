from pip._vendor.distlib.compat import raw_input
import  re
n=int(raw_input())
s=raw_input()
i=1
j=0
while i<n:
    if s[i]==s[i-1]:
        j+=1
    i+=1
print(j)