from pip._vendor.distlib.compat import raw_input

'''
j=1
j1=[]
k1=[]
for t in range(int(raw_input())):
    k=int(raw_input())
    for i in range(100):
        if k%6==0 and (k//6)%6==0 or k==6:
            k=k//6
            k1.append(k)
            if k==1:
                break
        else:
            k=k*2
            k1.append(k)
            if k==1:
                break
    k1.reverse()
    if k1.count(1)==0:
        kl=-1
        j1.append(kl)

    else:
        kl=len(k1)
        j1.append(kl)

for y in j1:
    print(y)
'''


'''def mul(k):
    k1=[]
    if k==1:
        return 0
    else:

        for i in range(100):

            if k % 6 == 0 and (k // 6) % 6 == 0 or k == 6:
                k = k // 6
                k1.append(k)
                if k == 1:
                    break

            else:
                k = k * 2
                k1.append(k)
                if k == 1:
                    break

        k1.reverse()
        if k1.count(1) == 0:
            kl = -1
        else:
            kl = len(k1)

    return kl
j1=[]
for t in range(int(raw_input())):
  k3=mul(int(raw_input()))
  j1.append(k3)
for t1 in j1:
    print(t1)'''

k1=[]
for t in range(int(raw_input())):
    k = int(raw_input())
    for i in range(50):
        if k % 6 == 0:
            k = k // 6
        elif k == 1:
            break
        else:
            k = k * 2

    if k != 1:
        i = -1

    k1.append(i)
for t1 in k1:
    print(t1)