k=[]
for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x=sum(a)
    l=x//n
    if x%n!=0:
        k.append(-1)
    else:
        d=[t for t in a if t>l]
        k.append(len(d))

for t in k:
    print(t)