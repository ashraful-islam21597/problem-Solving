from pip._vendor.distlib.compat import raw_input

l=[]
for t in range(int(raw_input())):
    k = []
    x,y,z=map(int,raw_input().split())
    k.append(min(x,y))
    k.append(min(x,z))
    k.append(min(y,z))
    s="NO"
    s1=""
    if  x==max(k[0],k[1]) and y==max(k[0],k[2]) and z==max(k[1],k[2]):
        s1=str(k[0])+" "+str(k[1])+" "+str(k[2])
        l.append("YES")
        l.append(s1)

    else:
        l.append("NO")

for t1 in l:
    print(t1)