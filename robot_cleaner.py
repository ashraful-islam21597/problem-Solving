k=[]

def forward(x,y,n,m):
    if x<n or y<m:
        if x>y:
            y=y+(n-x)
            x=n
            return x,y,(n-x)
        else:
            x=x+(m-y)
            y=m
            return x,y,(m-y)
def backward(x,y,n,m):
    if x<n or y<m:
        if x<y:
            y=y-((n-x)-(m-y)*2)
            x=n
            return x,y,((n-x)-(m-y)*2)
        else:
            x=x-((m-y)-(n-x)*2)
            y=m
            return x,y,((m-y)-(n-x)*2)
print(forward(7,2,10,9))
print(backward(10,5,10,9))
print(backward(6,9,10,9))
# for i in range(int(input())):
#     n, m, rb, cb, rd,cd=map(int,input().split())
#     lr=0
#     ll=0
#     x=0
#     for j in range(100):
#
#         if rb==n:
#             lr=1
#         elif cb==m:
#             ll=1
#         if rb==rd or cb==cd:
#             break
#         else:
#             if lr==0 and ll==0:
#                 rb=rb+1
#                 cb=cb+1
#                 x=x+1
#
#             else:
#
#                 if lr==1 and ll==0:
#                     rb=rb-1
#                     cb=cb+1
#                     x=x+1
#                 elif lr==0 and ll==1:
#                     rb=rb+1
#                     cb=cb-1
#                     x=x+1
#                 elif lr==1 and ll==1:
#                     rb=rb-1
#                     cb=cb-1
#                     x=x+1
#
#
#     k.append(x)
#
# for t in k:
#     print(t)



