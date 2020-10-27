from pip._vendor.distlib.compat import raw_input
def saw(n):

    k=[]
    k1=[]
    i=0
    for j in n:
        j=int(j)
        k.append(j)
    k.sort()
    while i<len(k)-1:
        a=k[i+1]
        b=k[i]
        m=a-b
        k1.append(m)
        i+=1
    k2=min(k1)

    return k2

p=[]
for t in range(int(raw_input())):
    n = raw_input()
    p1=saw(raw_input().split())
    p.append(p1)
for t1 in p:
    print(t1)









'''while j<len(s)-1:
    a=s1[j+1]
    max=a
    b=s1[j+1]
    max2=b
    m=s1[j+1]-s1[j]
    min=m
    if m<=min:
        if a>max and b>max2:
            s2=[a,b]

    print(s2)
    print(m)
    j+=1
'''