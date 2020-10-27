
from pip._vendor.distlib.compat import raw_input
k1=[]
for t in range(int(raw_input())):
    n=int(raw_input())
    m=raw_input().split()
    m1=max([int(j) for j in m])
    s=200*"a"
    k1.append(s[0:m1+1])
    for i in m:
        i=int(i)
        s1=s[0:i+1]+s[i+1:]
        if s1[i]=="a" and s[i]=="a":
            s1=s[:i]+str("b")+s[i+1:]
            s2=s1[0:m1+1]
            s=s1
            k1.append(s2)
        elif s1[i]=="b" and s[i]=="b":
            s1 = s[:i] + str("a") + s[i:]
            s2=s1[0:m1+1]
            s=s1
            k1.append(s2)
        else:
            s2=s1[0:m1+1]
            s=s1
            k1.append(s2)


for t1 in k1:
    print(t1)
































'''j=4
k1 = []
s=200*"a"
for t in range(int(raw_input())):
    n=int(raw_input())
    m=raw_input().split()
    i=0
    k1.append(s)
    m1=m[1:]
    j=int(m.pop())
    while i<len(m1):
        l=int(m1[i])
        l1=int(m[i])
        s3=""
        if l1<l:
            s1=l1*"a"+(l-1)*"b"
            s3 = s1
            k1.append(s1)


        else:
            s1 = l1 * "a" + (200-l)* "b"
            s3 = s1
            k1.append(s1)

        i+=1
    s2=s3[0:j]
    k1.append(s2)
for t1 in k1:
    print(t1)'''

