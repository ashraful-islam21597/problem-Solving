from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
m = raw_input()
l = m.split()
q = []
q1 = []
q2 = []
q3 = []
sum = 0
sum1 = 0
t = 0
for x in l:
    x = int(x)
    t = t + x
    if x == 4:
        q.append(x)
    elif x == 3:
        q1.append(x)
    elif x == 2:
        q2.append(x)
    else:
        q3.append(x)


i = q3 + q1
for c in i:
    sum = sum + c
for c1 in q2:
    sum1 = sum1 + c1
r = q.count(4)
if sum % 4 != 0:
    r1 = (sum // 4) + 1
else:
    r1 = int(sum / 4)

if sum1 % 4 != 0:
    r2 = (sum1 // 4) + 1
else:
    r2 = int(sum1 / 4)

s = r + r1 + r2
print(r)
print(r1)
print(r2)
print(s)