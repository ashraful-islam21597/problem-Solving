k=[]
for i in range(int(input())):
    s=input()
    if s.count("0") != s.count("1"):
        print(min(s.count("1"),s.count("0")))
        k.append(min(s.count("1"),s.count("0")))
    else:
        print(max(s.count("1"),s.count("0"))-1)
        k.append(k.append(max(s.count("1"),s.count("0"))-1))
# for j in k:
#     print(j)