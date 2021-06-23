from math import gcd
t=[]
for i in range(int(input())):
    n=int(input())
    count=0
    a=[int(i) for i in input().split()]

    for k in range(n):
        for k1 in range(k+1,n):
            if gcd(a[k],2*a[k1]) >1 or gcd(2*a[k],a[k1]) >1 :
                count=count+1
    t.append(count)
for l in t:
    print(l)
