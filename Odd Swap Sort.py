

k=[]
for j in range(int(input())):
    n=int(input())
    x=list(map(int,input().strip().split()))
    i=0
    pivot=0
    z=0
    s="YES"
    for i in range(n):
        if x[i]<pivot:
            if pivot%2==1:
                if x[i]%2==0:
                    if x[i]>=z:
                        print("ss")
                        z=x[i]
                    else:
                        print("nn",z)
                        s="NO"
                        break
                else:
                    s="NO"
                    break
            else:
                if x[i]%2!=0:
                    print(x[i])
                    if x[i]>=z:
                        z=x[i]
                    else:
                        s="NO"
                        break
                else:
                    s="NO"
                    break
        else:
            print(pivot,x[i])

            pivot=x[i]

    k.append(s)

for t in k:
    print(t)

