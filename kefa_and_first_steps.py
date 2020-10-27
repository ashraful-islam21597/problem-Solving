from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
m=raw_input().split()
m1=list(m)
l1=[]
l=[]
s1=''
s=''
for i in range(len(m1[0:len(m1)-1])):
    if m1[i]<=m1[i+1]:
        #l.append(m1[i])
        s=s+str(m1[i])
        s1=s
    else:
        continue
print(s1)


