from pip._vendor.distlib.compat import raw_input
x=int(raw_input())
n=raw_input().split()
y=[]
j=""
for i in range(1,x+1):
    x1=n.index(str(i))+1
    j=j+str(x1)+" "
print(j)
