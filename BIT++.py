from pip._vendor.distlib.compat import raw_input
n=int(raw_input())
i=0
j=0
while i<n:
    s=raw_input()
    if s=="X++" or s=="++X":
        j+=1
    else:
        j-=1
    i+=1
print(j)
