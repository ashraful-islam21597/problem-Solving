import re
for i in range(int(input())):
    s1={}
    a=[]
    n,m=map(int,input().split())
    for j in range(n):
        s=input()
        s1[j]=s
    count=0
    c=1
    for k in s1.values():
        if (re.search("RR",k))or(re.search("WW",k))or(re.search("R.W",k))or(re.search("W.R",k)):
            print("NO")
            break
        elif ("W" in k and((k.index("W")+1)%2)==0)or("R" in k and((k.index("R")+1)%2)!=0):
            if m==1:
                k="R"
            k="RW"*(m//2)+"R"*(m%2)
            a.append(k)
        elif ("R" in k and((k.index("R")+1)%2)==0)or("W" in k and((k.index("W")+1)%2)!=0) :
            if m==1:
                k="W"
            k="WR"*(m//2)+"W"*(m%2)
            a.append(k)
        else:
            t=count+1
            if t%2==0:
                k=a[0]
                k=k[::-1]
                a.append(k)
            else:
                k=a[0]
                a.append(k)
        count+=1
    s4=0
    for j1 in a:
        if (c%2!=0 and j1!=a[0])or(c==0 and j1!=a[0][::-1]):
            s4=0
            break
        else:
            s4=1
        c+=1
    if s4==1:
        print("YES")
        for t4 in a:
            print(t4)





