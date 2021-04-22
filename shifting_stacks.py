from pipenv.vendor.distlib.compat import raw_input
def get_cube_root(num):
    c=num ** (1/3)
    return c
for i in range(int(raw_input())):
    n=int(raw_input())
    n1=int(get_cube_root(n))
    
    for j in range(1,n1):
        c=j**3
        p=n-c
        b=get_cube_root(p)
        if b.is_integer():
            print(b)
