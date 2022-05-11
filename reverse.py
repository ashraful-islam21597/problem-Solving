for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    k=0
    s=''
    x=0
    z1=[]
    z=[]
    s1=''
    while k<n-1:
        if a[k]!=k+1:
            x=a.index(k+1)
            a[k],a[x]  = a[x],a[k]
            z=a[k+1:x][::-1]
            z1=a[0:k+1]+z+a[x:]
            break
        else:
            s1=s1+str(a[k])+" "
        k=k+1


    for j in z1:
        s=s+str(j)+" "
    if s!='':
        print(s)
    else:
        print(s1+str(a[-1]))

