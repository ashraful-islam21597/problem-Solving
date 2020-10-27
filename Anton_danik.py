from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
s=raw_input()
l=s.count("A")
l1=s.count("D")
if l>l1:
    print("Anton")
elif l1>l:
    print("Danik")
else:
    print("Friendship")
