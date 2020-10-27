from pip._vendor.distlib.compat import raw_input
k=[]
for t in range(int(raw_input())):
    a,b,c=map(int,raw_input().split())
    if a==(c/b) or a<(c/b):
        x=1
        y=-1
    elif (a>c) or a==c:
        x=-1
        y=b
    else:
        x=1
        y=b
    s=str(x)+" "+str(y)
    k.append(s)
for j in k:
    print(j)
