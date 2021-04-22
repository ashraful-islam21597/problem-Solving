from pipenv.vendor.distlib.compat import raw_input
t1=[]
def get_cube_root(num):
    c= num ** (1/3)
    return c

for i in range(int(raw_input())):
    n=int(raw_input())
    n1=int(get_cube_root(n))

    for j in range(1,n1):

        if ((j**3)+((n-j)**3))!=n:
            s="NO"
            continue
        else:
            s="yes"
            break
    t1.append(s)



        # if get_cube_root(n-j**3).is_integer():
        #
        #     s="YES"
        #     break
        # else:
        #     continue
    #t1.append(s)




# for i in range(int(raw_input())):
#     n=int(raw_input())
#     s="NO"
#     for j in range(n+1):
#         if j*j*j>n:
#
#             break
#         else:
#             x=get_cube_root(n-j*j*j)
#             if x==0:
#                 continue
#             else:
#                 s="YES"
#                 break
#     t1.append(s)







    # x=0
    # n1=int(raw_input())
    # n=raw_input().split()
    # for j in range(len(n)-1):
    #     k=max(int(n[j]),int(n[j+1]))
    #     k1=min(int(n[j]),int(n[j+1]))
    #     for i in range(1000):
    #
    #         k1=2*k1
    #         if k1<k:
    #             x=x+1
    #         else:
    #             break
    # t1.append(x)
for t in t1:
    print(t)


