from pipenv.vendor.distlib.compat import raw_input
s=0
for i in range(int(raw_input())):
    j,k=map(int,raw_input().split())
    for t in range(10000):
        if j>=k:
            if k>1:
                j=j//k
                k=k+1

            else:
                k=k+1
                s=s+1
            print(j,k,s)
        else:
            break

