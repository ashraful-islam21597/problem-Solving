k2=[]
k6=[]
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)+" "
    return str1
for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    k2=a
    k4=a
    for j in range(100):
        if 0 in k2:
            k2.remove(0)
        x=min(k2)
        if x<0:
            s='N0'
            k6.append(s)
            break
        elif x>0:
            k3=[]
            for j1 in a:
                if abs(j1-x) not in a and k2:
                    if j1==x:
                        continue
                    else:
                        k3.append(abs(j1-x))
                        k4.append(abs(j1-x))
                else:
                    continue
            if k3==[]:
                k4.append(0)
                k6.append("YES")
                k6.append(len(k4))
                d=listToString(k4)
                k6.append(d)
                break
            k2=k3
for t in k6:
     print(t)
