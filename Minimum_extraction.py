k2=[]
for i in range(int(input())):
    n=int(input())
    a=[int(j) for j in input().split()]
    a1=sorted(a)
    a1.reverse()
    k1=[]

    if len(a1)==1:
        k2.append(max(a1))
    else:
        for k in range(n-1):
            k1.append(a1[k]-a1[k+1])
        if max(k1)>=min(a1):
            k2.append(max(k1))
        else:
            k2.append(min(a1))

for t1 in k2:
    print(t1)
    # if len(a1)>=3:
    #     x=a1[n-2]-a1[n-3]
    #     x1=max(a1)-a1[n-3]
    #     if max(a1)==min(a1):
    #         print(max(a1))
    #     elif x1-x>x:
    #         print(x1-x)
    #
    #     else:
    #         print(x)
    # elif len(a1)==2:
    #     if max(a1)-min(a1)>min(a1):
    #         print(max(a1)-min(a1))
    #     else:
    #         print(min(a1))
    # else:
    #     x=a1[0]
    #     print(x)

