
for i in range(int(input())):
    list=[]
    a=input()
    for k in a:
        if int(a)%7==0:
            list.append(int(a))
            break
        else:
            for k1 in range(1,int(k)+1):
                s=a.replace(k,str(k1))
                if int(s)%7==0:
                    print(int(s))
                    list.append(a)
                break

    print(list)





