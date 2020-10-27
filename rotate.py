from pip._vendor.distlib.compat import raw_input
sum=0
q=[]
for i in range(int(raw_input())):
    exit,enter=map(int,raw_input().split())
    sum=(sum-exit)+enter
    q.append(sum)
    q1=max(q)
print(q1)
