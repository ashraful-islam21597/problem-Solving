k=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    s=input()
    if s == s[::-1] or b==0:
        k.append(1)
    else:
        k.append(2)
for j in k:
    print(j)
