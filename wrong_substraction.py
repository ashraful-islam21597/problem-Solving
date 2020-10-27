from pip._vendor.distlib.compat import raw_input

n,k=map(int,raw_input().split())
for x in range(k):
    if n%10==0:
        n=n/10
        n=int(n)
    else:
        n=n-1
print(n)