from pip._vendor.distlib.compat import raw_input

def str(l):
    j=0
    y=0
    y1=0
    k=[]
    for i in range(len(l)):

        if (i%2==0 and int(l[i])%2!=0) or (i%2!=0 and int(l[i])%2==0):
            j+=1
            k.append(l[i])
    for x in range(len(k)):
        if int(k[x])%2==0:
            y+=1
        else:
            y1+=1
    if y1==y:

        return j//2
    else:
        return -1

k2=[]

for k1 in range(int(raw_input())):
    n=int(raw_input())
    
    p=str(raw_input().split(),int(raw_input()))
    k2.append(p)
print(*k2,sep="\n")




