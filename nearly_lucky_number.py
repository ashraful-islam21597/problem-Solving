from pip._vendor.distlib.compat import raw_input

n=str(raw_input())
x=n.count("4")+n.count("7")
if x==4 or x==7:
    print("YES")
else:
    print("NO")