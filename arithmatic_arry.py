k=[]
for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x=sum(a)
    if x<1 or x<n:
        k.append(1)
    else:
        k.append(x-n)
for t in k:
    print(t)