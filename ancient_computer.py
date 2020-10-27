from pip._vendor.distlib.compat import raw_input

k=[]
def astr(n1,m1):
    j = 0
    m = max(n1, m1)
    n = min(n1, m1)

    for i in range(1, 100):
        x = divmod(m, n)
        if m == n:
            j = 0
            break
        elif x[0] % 8 == 0 and x[1] == 0:
            m = m / 8
            j += 1
            if m == n:
                break

        elif x[0] % 4 == 0 and x[1] == 0:
            m = m / 4
            j += 1
            if m == n:
                break
        elif x[0] % 2 == 0 and x[1] == 0:
            m = m / 2
            j += 1
            if m == n:
                break
        else:
            j = -1
    return j


for t in range(int(raw_input())):
    n1, m1 = map(int, raw_input().split())
    p=astr(n1,m1)
    k.append(p)
for t1 in k:
    print(t1)




