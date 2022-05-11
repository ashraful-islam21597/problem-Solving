k = []

for i in range(int(input())):
    n=int(input())
    a = list(map(int, input().strip().split()))
    s = "NO"
    s1=sorted(a)
    if a==s1:
        k.append("NO")
    else:
        k.append("YES")
for t in k:
    print(t)
