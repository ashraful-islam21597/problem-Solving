from pip._vendor.distlib.compat import raw_input


l=raw_input()[::-1]
l1=raw_input()
if l==l1:
    print("YES")
else:
    print("NO")
