
k=[]
for i in range(int(input())):
    n,h=map(int,input().split())
    x=input().split()
    l=[int(j) for j in x]
    m=max(l)
    l.pop(l.index(m))
    m1=max(l)
    d=h//(m+m1)
    d1=h-((m+m1)*d)

    if h<=m :
        k.append(1)
    elif 0<d1<=m:
        k.append(d*2+1)
    elif d1<=0:
        k.append(d*2)
    else:
        k.append(d*2+2)

for t in k:
    print(t)
