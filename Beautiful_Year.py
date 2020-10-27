from pip._vendor.distlib.compat import raw_input

n=int(raw_input())

def distinct(s):
    s1=""
    s2=0
    k=0
    for i in s:
        l=s.count(i)
        #print(l)
        if l>1 :
            break
        else:
            s1=s1+i
            if len(s)==len(s1):
                k=int(s1)
            else:
                continue
    return k

q2=[]

for x in range(n+1,90000):
    x1=str(x)
    q=distinct(x1)
    if q==0 :
        continue
    else:
        q2.append(q)



print(min(q2))






















