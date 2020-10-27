from pip._vendor.distlib.compat import raw_input
'''k=int(raw_input())
k2=[]
for x in range(k):
    n=int(raw_input())
    l=list(range(1,n+1))
    l.reverse()
    k1=[]
    j=1
    for i in l:
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i==j:
                    break
                else:
                    if i%k==0 and j%k==0:
                        k1.append(k)
                    else:
                        break
    k2.append(max(k1))
print(k1)
for z in k2:
    print(z)'''

'''n=int(raw_input())
l=list(range(1,n+1))
l.reverse()
k1=[]
k2=[]
for i in l:
    for j in range(1,n+1):

        if i==j:
            continue
        else:
            l = [i, j]
            k2.append(l)
            for k in range(1,n+1):
                if i%k==0 and j%k==0:
                    k1.append(k)
                else:
                   k1.append(1)'''
n=int(raw_input())
j=1
k2=[]
for i in range(2,n):
    for j in range(i+1,n+1):
        for k in range(1,n+1):
            if i>=k:
                #print(i, j, k)

                if i%k==0 and j%k==0:
                    k2.append(k)
                else:
                    break





print(k2)

