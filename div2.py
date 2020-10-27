from pip._vendor.distlib.compat import raw_input
'''
k1 = []
k2 = []
for t in range(int(raw_input())):
       n=int(raw_input())
       a=[int(i) for i in raw_input().split()]
       b=[int(j) for j in raw_input().split()]
       x=min(a)
       y=min(b)
       m=0
       k = 0
       while k<n:
           m=m+max((a[k]-x),b[k]-y)
           k+=1
       k2.append(m)
for t1 in k2:
    print(t1)
'''


s="8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888"
print(s.count("8"))





