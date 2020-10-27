from pip._vendor.distlib.compat import raw_input
n1=int(raw_input())
n=raw_input()
l1=n.split()
l=[]
c=0
for x in l1[0:n1]:
    c=int(x)
    l.append(c)
l.sort()
l.reverse()
sum=0
sum1=0
c=0
for i in l:
    sum=sum+int(i)
for j in l:
    sum1=sum1+int(j)
    if sum1<(sum-sum1) or sum1==(sum-sum1):
        c=c+1
    else:
        break

print(c+1)