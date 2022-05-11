import re
l=[]
for i in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    t=0
    if (a+b)>0 or len(s)==1:
        t=len(s)*a+b*len(s)
    else:
        k=[len(j) for j in re.findall(r'(?:1)+', s)]
        k1=[len(j) for j in re.findall(r'(?:0)+', s)]
        s1=0
        if len(k)>len(k1):
            if k1==[]:
                s1=b
            else:

                for y in k1:
                    s1=s1+(a*y+b)

            s2=a*sum(k)+b
            t=s1+s2
        else:
            if k==[]:
                s1=b
            else:

                for y in k:
                    s1=s1+(a*y+b)
            s2=a*sum(k1)+b
            t=s1+s2

    l.append(t)
for t1 in l:
    print(t1)


# groups = re.findall(r'(?:1)+', s)
# groups1 = re.findall(r'(?:0)+', s)
# k=[len(j) for j in groups]
# k1=[len(j) for j in groups1]
# if len(k)>len(k1):
#
#     if (a>1 and b<1)or(a<1 and b>1):
#         #x=sum([a*y+y*b for y in k1])
#         x=a*len(k1)+b*len(k1)
#         k=a*len(k)+b*len(k)
#         t=x+k
#     else:
#         x=sum([a*y+b for y in k1])
#         k=sum(k)*a+b
#         t=x+k
#     # k1=[len(y) for y in k1]
#     # print(k1)
#     # for j in k1:
#     #     t=t+(a*j+b)
#     # t=t+(a*(sum(k))+b)
# else:
#     x=sum([a*y+b for y in k])
#     if (a>1 and b<1)or(a<1 and b>1):
#
#         k1=a*len(k1)+b*len(k1)
#         t=x+k1
#     else:
#         k1=sum(k1)*a+b
#         t=x+k1
#
#     # k1=[len(y) for y in k]
#     # print(k)
#     # for j in k:
#     #     t=t+(a*j+b)
#     # t=t+(a*(sum(k1))+b)