from pip._vendor.distlib.compat import raw_input
k=[]
for j in range(int(raw_input())):
    s2=""
    n=int(raw_input())
    s=raw_input().split()
    i=1
    while i<n-1:
        s1="NO"
        if int(s[i-1])<int(s[i]) and int(s[i+1])<int(s[i]):
            s1="YES"

            s2=s2+str(i)+" "+str(i+1)+" "+str(i+2)

            break
        else:
            i+=1
            continue
        i+=1
    k.append(s1)
    k.append(s2)

for t1 in k:
    print(t1)
