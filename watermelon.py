from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
s=""
if n%2==0 and n !=2 :
    print("YES")
else:
    print("NO")
'''for i in range(1,n):
    if i%2==0:
        x=n-i
        if x%2==0 and x+i==n:
            s="YES"
        else:
            s="NO"
    
print(s)'''
