from pipenv.vendor.distlib.compat import raw_input
def get_cube_root(num):
    c= num ** (1/3)
    return c
# t1=[]
# for i in range(int(raw_input())):
#     x=int(raw_input())
#     x1=int(get_cube_root(x))
#     s="NO"
#     for j in range(x1+1):
#         p=x-j**3
#         p1=x-p
#         if get_cube_root(p1).is_integer():
#             s="YES"
#             break
#         else:
#             continue
#     t1.append(s)
# for t in t1:
#     print(t)

t1=[]
for i in range(int(raw_input())):
    x=int(raw_input())
    n=int(get_cube_root(x))
    s="NO"
    for j in range(n+1):

        p=j**3
        p1=(x-p)
        if float(get_cube_root(p1)).is_integer():
            s="YES"
            break
        else:
            continue
        # s="NO"
        # if float(get_cube_root(x-i**3)).is_integer():
        #     s="YES"
        #
        #     break
        # else:
        #     continue

    t1.append(s)
for k in t1:
    print(k)
#
#     # if get_cube_root(x-i**3).is_integer():
#     #     print("yes")
#     #     break
#     # else:
#     #     print("False",i)
#     #     continue