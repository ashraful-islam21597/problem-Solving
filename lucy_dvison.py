from pip._vendor.distlib.compat import raw_input

n=int(raw_input())

l=[4,7,47,77,444,447,477,744,747,777,]
s=""
for i in l:
    if n%i!=0:
        s="NO"
        continue
    else:
        s="YES"
        break
print(s)