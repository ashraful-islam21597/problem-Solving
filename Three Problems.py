n=int(input())
a=list(map(int,input().strip().split()))
b=set(a)
s=''
for j in range(3):
    x=min(b)
    s=s+str((a.index(x)+1))+" "
    b.remove(x)
print(s)