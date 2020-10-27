from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
i=0
j=0
while i<n:
    s,t=map(int,raw_input().split())
    if t-s>=2:
        j+=1
    i+=1
print(j)