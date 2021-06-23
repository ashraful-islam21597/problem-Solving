
n,q=map(int,input().split())
k1=[]
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#k=[alphabet.index(j)+1 for j in input()]
k=[]
d=0
for j in input():
    d=d+(alphabet.index(j)+1)
    k.append(d)
for i in range(q):
    l,r=map(int,input().split())
    x=0
    if l>1:
        x=k[r-1]-k[(l-1)-1]
    else:
        x=k[r-1]
    k1.append(x)
for t in k1:
    print(t)
