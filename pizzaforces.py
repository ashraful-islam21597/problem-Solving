
k1=[]
for i in range(int(input())):
    p=int(input())
    if p>6 and p%2!=0:
        p=p+1
    p1=p//10
    p2=p//8
    p3=p//6
    n=0
    x=0
    for j in range(0,10000):
        p6=(p3-n)*6
        p4=p-p6
        if p4%8==0 or p4==0:
            x=(p3-n)*15+(p4//8)*20
            break

        elif p4%10==0 or p4==0:
            x=(p3-n)*15+(p4//10)*25
            break
        n=n+1
    if p<6:
        x=15
    k1.append(x)
for t in k1:
    print(t)






















#     if (p%10==0):
#         x=(p//10)*25
#     elif p%6==0:
#         x=(p//6)*15
#     elif p%8==0:
#         x=(p//8)*20
#     else:
#         if p>=10:
#             if p%10>=8:
#
#                 x=((p//10)+1)*25
#             elif 8>p%10>6:
#                 x=(p//10)*25+20
#             else:
#                 x=(p//10)*25+15
#         elif 8<p<10:
#             x=25
#         elif 6<p<8:
#             x=20
#         else:
#             x=15
#
#
#     k.append(x)
# for t in k:
#     print(t)