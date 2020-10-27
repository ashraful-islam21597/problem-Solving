from pip._vendor.distlib.compat import raw_input

'''
def binary(n):
    i=n%2
    if n/2==0:
        return n
    else:
        s=str(binary(n//2))+str(i)
        return s
n=raw_input()
x=[binary(int(i))[1:] for i in n]
s=""'''
'''k=[]
for t in range(int(raw_input())):
    n=int(raw_input())
    if n<4:
        x=n-1
        s=x*"9"+"8"
        k.append(s)
    else:
        x=n-((n+3)//4)
        s=x*"9"+((n+3)//4)*"8"
        k.append(s)
for t1 in k:
    print(t1)'''

for i in range(5):
    print(i)