
from pip._vendor.distlib.compat import raw_input
'''for t in range(int(input())):
    n=int(input())
    s=input()
    s1=s[0:len(s)-(n-1)]
    i=0
    k=[]
    k1=[]
    for j in range(len(s1)):
        s2=s[j:j+n]

        k.append(s[j:j+n])
        #print(s[j:j+n])

d="1111"
s3=''
x=0
for t1 in k:
    if d[x]==t1[x]:
        s3=t1[x]
    else:
        x=x+1
    s3=s3+t1[x]

print(s3[0:n])'''
def sub(x,k,i):
    if (x-i)-i==k:
        return 0
    elif (x-i)-i<k:
        x+=1
        return 1
    else:
        i+=1
        return sub(x,k,i)


z = []
c=0
for t in range(int(raw_input())):
    x, k = map(int, raw_input().split())
    if k != 0:

        if x <= k:
            c=k-x
            z.append(c)
        else:
            for i in range(100000000):
                j=0
                if sub(x,k,j)==0:

                    z.append(i)
                    break
                else:
                    x+=1



    else:
        if x % 2 != 0:
            z.append(1)
        else:
            z.append(0)

for t1 in z:
    print(t1)