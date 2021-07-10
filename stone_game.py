k=[]
for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x=a[::-1]
    mini1=x.index(min(x))+1
    maxi1=x.index(max(x))+1
    mini=a.index(min(a))+1
    maxi=a.index(max(a))+1
    q=(max(mini,maxi))
    q2=(max(mini1,maxi1))
    q1=(min(mini,mini1)+min(maxi,maxi1))
    k.append(min(q,q1,q2))


for t in k:
    print(t)