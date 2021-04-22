
k2=[]
for i in range(int(input())):
    k1=[]
    s='1'
    n,k=map(int,input().split())
    if n//2<k or (n<=2 and k!=0):

        k2.append(-1)
    elif n%2==0 and n//2-1<k:
        k2.append(-1)

    else:
        count=0
        for j in range(2,n+1):
            if j%2==0:
                if count==k :
                    s=s+" "+str(j)
                    k1.append(j)
                else:
                    s=s+" "+str(j+1)
                    k1.append(j+1)
                    count+=1
            else:
                if count==k:
                    if j in k1:
                        s=s+" "+str(j-1)
                        k1.append(j-1)
                    else:
                        s=s+" "+str(j)
                        k1.append(j)
                else:
                    s=s+" "+str(j-1)
                    k1.append(j-1)

        if n%2==0 :
            k1.pop()
            if str(n) in s:
                s.replace(str(n),'')
            else:
                s=s[0:len(s)-1]
            #s=s+str(n)
            k1.append(n)
        k1.insert(0,1)

        k2.append(s)

for t in k2:
    print(t)
