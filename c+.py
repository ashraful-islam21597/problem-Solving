from pip._vendor.distlib.compat import raw_input

t=int(raw_input())
def operation(a,b,n):
    i=0
    j=0
    while i<=n:
        j += 1
        a1 = max(a, b)
        b1 = min(a, b)
        a1 += b1
        a = a1
        b = a1 - b1
        i=a
    return j
s1=[]
for x in range(t):
    a, b, n = map(int, raw_input().split())
    s=operation(a,b,n)
    s1.append(s)
for i in s1:
    print(i)
