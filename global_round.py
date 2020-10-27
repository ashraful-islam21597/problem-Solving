from pip._vendor.distlib.compat import raw_input
'''def loop(i, j):
    if j!=i:
        j += 1
        x=int(input())

    else:
        return 0
    return loop(i, j)




a=int(input())
b=a-a
k=['a','b','c','d',]
print(k[loop(a,b)])'''

def sub(x,k,i):
    if (x-i)-i==k:
         return 0
    elif (x-i)-i<k:
         return 1
    else:
        i+=1
        return sub(x,k,i)
print(sub(734452,18288,0))
'''c=0
x,k=map(int,input().split())
for i in range(1000000000):
    j=0
    if sub(x,k,j)==0:
        print(c)
        break
    else:
        c+=1
        x+=1'''






















'''k=[]
for t in range(int(raw_input())):
    n=int(raw_input())
    a=[int(j) for j in raw_input().split()]
    if a.count(a[0])==len(a):
        k.append(len(a))
    else:
        k.append(1)

for t1 in k:
    print(t1)'''





