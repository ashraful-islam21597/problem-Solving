from pip._vendor.distlib.compat import raw_input


def array(l, n):
    j = 0
    k = []
    for i in range(l):
        if i % 2 == int(n[i]) % 2:
            j += 1
        else:
            k.append(n[i])
    if len(k) == 0:
        return 0
    elif k.count(k[0]) == len(k):
        return -1

    else:
        if len(k) % 2 == 0:
            return (len(k) // 2)
        else:
            return -1


k1 = []
for j in range(int(raw_input())):
    l = int(raw_input())
    n = raw_input().split()
    p = array(l, n)
    k1.append(p)
for t in k1:
    print(t)



