k=[]
for t in range(int(input())):
    n,m,i,j=map(int,input().split())
    s=''
    if (i,j)==(1,1):
        if m>j:
            x,y=(1,2)
        elif n>i:
            x,y=(2,1)
        else:
            x,y=(1,1)
        a,b=(n,m)
        s=str(x)+" "+str(y)+" "+str(a)+" "+" "+str(b)
    elif(i,j)==(n,m):
        x,y=(1,1)
        if n>1 and m>1:
            (a,b)=(n-1,m-1)
        elif n>1 and m<=1:
            (a,b)=(n-1,m)
        elif m>1 and n<=1:
            (a,b)=(n,m-1)


        s=str(x)+" "+str(y)+" "+str(a)+" "+" "+str(b)
    else:
        x,y=(1,1)
        a,b=(n,m)
        s=str(x)+" "+str(y)+" "+str(a)+" "+" "+str(b)
    k.append(s)
for j in k:
    print(j)





