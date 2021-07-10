# for i in range(int(input())):
#     a,b=map(int,input().split())
#     if b>1:
#         if (a*(b-1)+a*(b+1))%(a*b)==0 and a!=b:
#             print("YES")
#             print(a,a*(b+1),((a+a*(b+1))))
#         else:
#             print("NO")
#     else:
#         if (a*(b+1)+a*(b+2))%(a*b)==0 and a!=b:
#             print("YES")
#             print((a*(b+1)),a*(b+2),((a*(b+1)+a*(b+2))))
#         else:
#             print("NO")

for i in range(int(input())):
    a,b=map(int,input().split())

    if (a*(b-1)+a*(b+1))%(a*b)==0  and b!=1:
        print("YES")
        print((a*(b-1)),a*(b+1),((a*(b-1)+a*(b+1))))
    else:
        print("NO")