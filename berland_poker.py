from pip._vendor.distlib.compat import raw_input

a = []
for i in range(int(raw_input())):
	n, m, k = map(int, raw_input().split())
	card = n // k
	if card >= m:
		a.append(m)
	else:
		if n == m:
			a.append(0)
		elif n == k and m == 1:
			a.append(1)
		elif n == k and m != 1:
			a.append(0)
		else:
			x = m - card
			k1 = k - 1
			if card == x:
				if k1 == 1:
					a.append(0)
				else:
					a.append(1)
			else:
				d=divmod(m,k)
				if d[1]!=0:
					d2=d[0]+1
				else:
					d2=d[0]
				y=card-d2
				a.append(y)

for j in a:
	print(j)

