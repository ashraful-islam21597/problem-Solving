from pip._vendor.distlib.compat import raw_input
k=[]
for i in range(int(raw_input())):
    l, r = map(int,raw_input().split())
    if r%2==0:
        x=float((r/2))+ 0.5
    else:
        x=(r+1)/2

    if float(l)>=float((r+1)/2):
        k.append("YES")
    else:
        k.append("NO")
for t in k:
    print(t)



