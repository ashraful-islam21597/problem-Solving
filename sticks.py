from pip._vendor.distlib.compat import raw_input
'''k=[]
for i in range(int(raw_input())):
    n=int(raw_input())
    k.append(((n-1)//2)+1)

for j in k:
    print(j)'''
j=int(input())
k=j
i=0
while k>=1:
    i1=j-k
    i=i1*2+1
    s=k*" "
    s1=i*"*"
    s3=s+s1
    print(s3)
    k-=1




