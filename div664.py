from pip._vendor.distlib.compat import raw_input
k1=[]

for t in range(int(raw_input())):
    c1=0
    c=int(raw_input())
    m=raw_input()
    l1= [int(i) for i in m]


    for i in range(len(l1) + 1):
        for j in range(i + 1, len(l1) + 1):
            sub = l1[i:j]
            if sum(sub)==len(sub):
                c1+=1
            else:
                continue
    #l1=list(m)
    #k = sub_lists(l1)
    k1.append(c1)

for t1 in k1:
    print(t1)