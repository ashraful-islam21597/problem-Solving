from pip._vendor.distlib.compat import raw_input
'''k=[]
for i in range(int(raw_input())):
    n,m=map(int,raw_input().split())
    k.append(min(max(2*n,m),max(n,2*m))**2)

for j in k:
    print(j)'''
'''k=[]

for i in range(int(raw_input())):
    n=int(raw_input())
    s = ""
    for j  in range(0,n):
        s=s+str("1")+" "
    k.append(s)

for t in k:
    print(t)
'''


'''def compute(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


k = 0
k1 = 0
k3 = []
for t1 in range(int(raw_input())):
    n = int(input())
    s = list(range(1, n))
    s1 = " "
    h = n

    for i in s:
        x = i
        y = n - i
        g = compute(x, y)

        if g < h:
            h = g
            k = x
            k1 = y

        else:
            continue
    s1 = str(k) + " " + str(k1)
    k3.append(s1)
for t in k3:
    print(t)'''
'''k3=[]
for t1 in range(int(raw_input())):
    n = int(input())
    n1=list(range(1,(n//2)))
    n1.reverse()
    for i in n1:
        if n%i==0:
            k=i
            k1=n-k
            break
        else:
            continue
    s1 = str(k) + " " + str(k1)
    k3.append(s1)

for t in k3:
    print(t)'''
k=list(range(1,1000))
print(*k,sep=" ")

