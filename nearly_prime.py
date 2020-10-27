from pip._vendor.distlib.compat import raw_input
k=[]
for t in range(int(raw_input())):
    n=int(raw_input())
    if n<=30:
        k.append("NO")
    else:
        k.append("YES")
        if n-30==6 or n-30==10 or n-30==14:
            k.append(f'{6} {10} {15} {n-31}')
        else:
            k.append(f'{6} {10} {14} {n-30}')
for t1 in k:
    print(t1)