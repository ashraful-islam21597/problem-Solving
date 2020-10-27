import re
pattern=r"1"
i = 1
s=""
c = 0
while i<=1000000000000000:
    s = s + str(i)
    l=re.findall(pattern,s)
    if len(l)==10000000:
        print(i)
        break
    i+=1
print(s)
print(len(s))
print(l)
print(len(l))