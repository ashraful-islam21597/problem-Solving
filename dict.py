from pip._vendor.distlib.compat import raw_input

k2=[]
j=0
x=0
for t in range(int(raw_input())):
    k1 = []
    n,k,z=map(int,raw_input().split())
    a=[int (y)for y in raw_input().split()]
    a1=a[0:k+1]
    i=k
    b=0
    c=0
    q=0
    while i>0:
        j=k-i
        b=b+a1[j]
        path=k-c
        p=divmod(path,2)
        l=p[0]
        l1=p[0]+p[1]
        if l<=z:
            x=a1[j]*l+a1[j+1]*l1+b
            k1.append(x)

        else:

            #x = a1[j] * z + a1[j + 1] * l1 + b
            #x=sum(a1[:k-z-1])+max(a1[:k-z])*z+a1[a1.index(max(a1[:k-z]))+1]
            x=a1[j]*z+a1[j+1]*(z+1)+sum(a1[c+2:(k-(z*2+1))+1])+b
            k1.append(x)



        c+=1
        i-=1
    y=max(k1)
    k2.append(y)


for t1 in k2:
    print(t1)


print(k1)