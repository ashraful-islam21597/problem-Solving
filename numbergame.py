from pip._vendor.distlib.compat import raw_input

k = []


def xtra(n):
    s = ""
    n = int(n)
    if n % 2 != 0:
        if n == 1:
            s = "FastestFinger"
            # k.append("FastestFinger")
        else:
            s = "Ashishgup"
            # k.append("Ashishgup")
    elif n == 2:
        s = "Ashishgup"
        # k.append("Ashishgup")
    else:
        n3 = divmod(n, 4)
        n1 = list(n3)
        if (n1[0]) % 4 == 0 and n1[1] == 0 or n == 8 or n == 1:
            s = "FastestFinger"
        else:

            l = [x for x in range(1, n) if x % 2 != 0]
            l.reverse()
            for i in l:
                if (n / i) % 4 == 0:
                    s = "Ashishgup"
                    # k.append("Ashishgup")


                else:
                    k1 = n // 2
                    q = 0
                    for i in range(2, k1):
                        if k1 % i == 0:
                            q = 1
                            break

                        else:
                            q = 0
                            continue

                    if q == 0:
                        s = "FastestFinger"
                        # k.append("FastestFinger")
                        break

                    else:
                        s = "Ashishgup"
                        # k.append("Ashishgup")
                        break
    return s


for c in range(int(raw_input())):
    s = xtra(raw_input())
    k.append(s)
for i in k:
    print(i)