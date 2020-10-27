from collections import deque

s="aaababba"
t="abbbaaaa"
count=0
x=list(s)
y=list(t)
q=[]
q1=[]
q2=[]
for i,j in enumerate(x):
    for n,m in enumerate(y):
        if i==n and j == m:
               x.reverse()
               y.reverse()
               x.pop()
               y.pop()
               x.reverse()
               y.reverse()
               if i==n and j is not m:
                   break





print(q)
print(q1)
l=len(q)-1

i=0
for z in list(range(l)):

    if q==q1:
        break

    else:
        count += 1
        q2 = list(q.pop())
        q = q2 + q
        print(q)





print(count)


'''for k1 in q1:
    l=q.pop()
    if k1 is not l:

        count+=1
        continue
    else:
        break'''








'''string=''
x=list(s)
y=list(t)
z=''
for i in x:
    for j in y:
        if i is not j:
            d=x.pop()
            z=d+z
        else:
            continue
e=""
z1=list(z)
z2=list(z1.pop())
for i in z2:
 f=list(z1.pop())+z1
 n=x+f
 n1=n+z2
 if str(n1)==t:
     i=1
 else:
     i=2


print(i)
'''

'''print(x)
z1=list(z)
z2=list(z1.pop())
n=x+z1
n1=n+z2
print(n1)
print(z1)
'''



