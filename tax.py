from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
m = raw_input()
l = m.split()
sum = 0
q = []
q1 = []
q2 = []
q3 = []
t = []
for x in l:
    x = int(x)

    if x == 4:
        q.append(x)
    elif x == 3:
        q1.append(x)
    elif x == 2:
        q2.append(x)
    else:
        q3.append(x)

a = q1.count(3)
b = q2.count(2)
c = q3.count(1)
p = min(a, c)
i = q1 + q3 + q
m = min(a, c)
j = q3[m:] + q2 + q1[m:]
p = i.count(4) + m
if j.count(1) == 0:
    g1c = j.count(3)
    g2c = j.count(2) * 2
    if g2c % 4 == 0:
        g2c = g2c // 4
    else:
        g2c = (g2c // 4) + 1
    s = g1c + g2c + p
else:

    for d in j:
        sum = sum + d

    if sum % 4 == 0:
        d1 = (sum // 4)
        s = d1 + p
    else:
        d1 = (sum // 4) + 1
        s = d1 + p

print(s)