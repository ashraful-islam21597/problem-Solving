from pip._vendor.distlib.compat import raw_input
k=[]
for t in range(int(raw_input())):
    n=int(raw_input())
    m=[int(i) for i in raw_input().split()]
    m.sort()
    m.reverse()
    s=0
    i=0
    s1="YES"
    while s<len(m[0:]):
        i=m[s-1]-m[s]
        if i>1:
            s1="NO"
            break
        s+=1
    k.append(s1)
for t1 in k:
    print(t1)



