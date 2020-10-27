from pip._vendor.distlib.compat import raw_input
import re
n = int(raw_input())
j5=[]
for x in range(n):
    k,n=map(int,raw_input().split())
    s =raw_input()
    j = 1
    a = 0
    if s.count("1")==0 :
            while j<=k:
                a += 1
                j += n
                j += 1
            j5.append(a)
    else:
        x = re.split("1", s)
        j2 = (len(x.pop())) // (n + 1)
        x.reverse()
        j3 = (len(x.pop())) // (n + 1)
        x.reverse()
        j1 = 0
        for i in x:
            s1 = len(i) % (n + 1)
            if s1 < n:
                j = (len(i) // (n + 1)) - 1
                j1 += j
            else:
                j = (len(i) // (n + 1))
                j1 += j
        j4=j1 + j2 + j3
        j5.append(j4)
for i in j5:
    print(i)
