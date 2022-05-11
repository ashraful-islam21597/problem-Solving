import datetime
import math
import re
import string
from math import gcd
# l,r=map(int,input().split())
# s=[]
# for i in string.ascii_lowercase:
#     s.append(i)
# print(s)

#list(sorted(lst, key=lambda x: [x % 2, x]))
# def gcd(x,y):
#     if y==0:
#         return x
#     return gcd(y,x%y)

# def  sum_of_digit(n):
#
#     if n%2!=0:
#         x=n//2
#         sum=x*(n+1)+(x+1)
#
#     else:
#         x=n//2
#         sum=x*(n+1)
#     return sum
#
# print(sum_of_digit(int(input())))
#s=['abc','xyz']
# print(s[0][::-1])

# for i in range(int(input())):
#     a=[]
#     s6=''
#     s7=''
#     s=''
#     s1=""
#     s5=''
#     n,m=map(int,input().split())
#     if m==1:
#         k="R"
#         k1="W"
#         s6="RW"*(n//2)+"R"*(n%2)
#         s7="WR"*(n//2)+"W"*(n%2)
#         for c in s6:
#             s=s+"\n"+c
#         for c in s7:
#             s1=s1+"\n"+c
#
#     else:
#         k="RW"*(m//2)+"R"*(m%2)
#         k1="WR"*(m//2)+"W"*(m%2)
#         for j in range(n):
#             s=s+'\n'+k[::-1]
#             s6=s6+k[::-1]
#             s1=s1+'\n'+k1[::-1]
#             s7=s7+k1[::-1]
#             k=k[::-1]
#             k1=k1[::-1]
#
#
#
#     for k in range(n):
#         s5=s5+str(input())
#     p1=1
#     for x,y in enumerate(s5):
#         if y=='.':
#             continue
#         else:
#             if y!=s6[x]:
#                 p1=1
#             else:
#                 p1=0
#                 break
#     for x,y in enumerate(s5):
#         if y=='.':
#             continue
#         else:
#             if y!=s7[x]:
#                 p1=1
#             else:
#                 p1=0
#                 break
#     if p1==1:
#         l=s5.index("W")+1
#         if l%2==0:
#             print("YES")
#             print(s)
#         else:
#             print("YES")
#             print(s1)
#     else:
#         print("NO")

# for i in range(int(input())):
#     a=[]
#     s6=''
#     s7=''
#     s=''
#     s1=""
#     s5=''
#     n,m=map(int,input().split())
#     if m==1:
#         k="R"
#         k1="W"
#         s6="RW"*(n//2)+"R"*(n%2)
#         s7="WR"*(n//2)+"W"*(n%2)
#         for c in s6:
#             s=s+"\n"+c
#         for c in s7:
#             s1=s+"\n"+c
#     else:
#         k="RW"*(m//2)+"R"*(m%2)
#         k1="WR"*(m//2)+"W"*(m%2)
#
#
#         for j in range(n):
#             s=s+'\n'+k[::-1]
#             s6=s6+k[::-1]
#             s1=s1+'\n'+k1[::-1]
#             s7=s7+k1[::-1]
#             k=k[::-1]
#             k1=k1[::-1]
#     for k in range(n):
#         s5=s5+str(input())
#     p1=1
#
#     for x,y in enumerate(s5):
#         if y=='.':
#             continue
#         else:
#             if y!=s6[x] or y!=s7[x]:
#                 p1=1
#             else:
#                 p1=0
#                 break
#     if p1==1:
#         l=s5.index("W")+1
#         print("YES")
#         print(p1)
#         if l%2==0:
#             s=s[::-1]
#
#
#             s, result = s[:-1], s[-1]
#             print(s)
#         else:
#             s1=s1[::-1]
#
#             s1, result = s1[:-1], s1[-1]
#             print(s1)
#     else:
#         print("NO")
# k2=[]
# for i in range(int(input())):
#     a=[]
#     s=''
#     s1=""
#     s5=''
#     s6=''
#     s7=''
#     n,m=map(int,input().split())
#     if m==1:
#         k="W"
#         k1="R"
#         s6="RW"*(n//2)+"R"*(n%2)
#         s7="WR"*(n//2)+"W"*(n%2)
#         for c in s6:
#             s=s+"\n"+c
#
#         for c in s7:
#             s1=s1+"\n"+c
#         s=s[::-1]
#         s, result = s[:-1], s[-1]
#
#         s1=s1[::-1]
#         s1, result1 = s1[:-1], s1[-1]
#
#     else:
#         if m%2!=0:
#             k="WR"*(m//2)+"W"
#             k1="RW"*(m//2)+"R"
#         else:
#             k="WR"*(m//2)
#             k1="RW"*(m//2)
#
#         for j in range(n):
#             if (j+1)%2!=0:
#                 if (j+1)==n:
#                     s=s+k
#                     s1=s1+k1
#                     s6=s6+k
#                     s7=s7+k1
#                 else:
#                     s=s+k+'\n'
#                     s1=s1+k1+'\n'
#                     s6=s6+k
#                     s7=s7+k1
#             else:
#                 if (j+1)==n:
#                     s=s+k1
#                     s1=s1+k
#                     s6=s6+k1
#                     s7=s7+k
#                 else:
#                     s=s+k1+'\n'
#                     s1=s1+k+'\n'
#                     s6=s6+k1
#                     s7=s7+k
#     for k in range(n):
#         s5=s5+str(input())
#     p1=''
#     p2=""
#
#     for p,q in enumerate(s5):
#         if p=='.':
#             continue
#         else:
#             if q==s6[p]:
#                 p1=p1+"0"
#                 break
#     for x,y in enumerate(s5):
#         if y=='.':
#             continue
#         else:
#             if y==s7[x]:
#                 p1=p1+"0"
#                 break
#     if p1!="00":
#         k2.append("YES")
#         if "R" in s5 and "W" not in s5:
#             l=s5.index("R")+1
#             if l%2!=0:
#                 k2.append(s1)
#             else:
#                 k2.append(s)
#         elif "W" in s5 and "R" not in s5:
#             l=s5.index("W")+1
#             if l%2!=0:
#                 k2.append(s)
#             else:
#                 k2.append(s1)
#         else:
#             l=min((s5.index("W")+1),(s5.index("R")+1))
#
#             if l%2!=0:
#                 if s5[l]=="W":
#                     k2.append(s)
#                 else:
#                     k2.append(s1)
#             else:
#                 if s5[l]=="W":
#                     k2.append(s1)
#                 else:
#                     k2.append(s)
#     else:
#         k2.append("NO")
#
# for t in k2:
#     print(t)

def counter(x,x1,y):
    a=x//y
    l=list(range(1,y+1))
    l.reverse()
    alphabet=list(string.ascii_uppercase)
    slot=dict(zip(l,alphabet))
    r=list(range(len(slot)))
    r.reverse()
    max=y+1
    if math.ceil(x1/a) in slot:
        return slot[math.ceil(x1/a)],datetime.time(9+r[math.ceil(x1/a)-1],00,00),datetime.time(9+r[math.ceil(x1/a)-1]+1,00,00)
    # elif math.ceil(x1/a)==max:
    #     return slot[math.ceil(x1/a)-1],datetime.time(9+r[max-2],00,00),datetime.time(9+r[max-2]+1,00,00)

# k=list(range(1,9))
# k.reverse()
# for i in k:
#     k,l,j=(counter(8,i,4))
#     print(k,i)

print(math.ceil(17/8))