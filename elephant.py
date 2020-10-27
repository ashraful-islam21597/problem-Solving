from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
c=0
if n>5:
    c=n//5
    c1=n%5
    if c1!=0:
        c=c+1
else:
    c=1
print(c)


