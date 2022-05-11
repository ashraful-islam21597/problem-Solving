# k=[5,4,2,3,6,1]
# i=1
#
# for i in range(1,len(k)):
#     for j in range(-i,1 ):
#         print(i,j)

# k1=[]
# for t in range(int(input())):
#     k=[]
#     n=int(input())
#     a=list(map(int,input().split()))
#     for i in range(len(a)+1):
#         for j in range(i):
#             k.append(a[j:i])
#     y=0
#     for j in k:
#         y=y+(len(j)+j.count(0))
#     k1.append(y)
#
# for t1 in k1:
#     print(t1)


# a1=[]
# l1=a
# for i in range(len(a)):
#     l=[]
#     l.append(a[i])
#     a1.append(l)
#     s=a[i:]
#     s1=a[:-(i+1)]
#     print(s,s1)
#     if s not in a1 and s!=s1:
#         a1.append(a[i:])
#     if s1 not in a1 and s!=s1:
#         a1.append(a[:-(i+1)])

# a1.remove([])
# print(a1)
# q2=min(a)
# a.pop(a.index(q2))
# q1=min(a)
# print(q1)
# x1=[]
# for j in k:
#     q=len(j)
#     if min(j)==max(j) and max(j)>=q1:
#         x1.append(q+q2)
#     else:
#         x1.append(q+q1)
# print(sum(x1))


import math
def prime_factor(x):
    #x = int(input())
    divisors = [i for i in range(2, (x // 2) + 1) if x % i == 0]  # divisor of x from 2 to s/2

    prime_divisors = []

    for divisor in divisors:  # prime divisor of x
        prime = divisor
        y = math.sqrt(divisor) + 1  # square root of each divisor
        for i in range(2, int(y)):
            if divisor % i == 0:
                prime = 0
                break
            else:
                prime = divisor
        if prime != 0:
            prime_divisors.append(prime)

    if prime_divisors == []:
        prime_divisors.append(x)

    string = str(x) + " = "

    for factor in prime_divisors:  # to generate a string by the prime factors
        while x % factor == 0:
            string = string + str(factor) + " X "
            x = x // factor
    return (string[:-2])
for i in range(0,5):
    print(prime_factor(int(input())))

# import math
# x=int(input())
# k=[]
#
# for i in range(2,(x//2)+1):
#     if x%i==0:
#         k.append(i)
# k1=[]
# s1=str(x)+"="
# c=1
# for j in k:
#     s=j
#     y=math.sqrt(j)+1
#     for i in range(2,int(y)):
#         if j%i==0:
#             s=0
#             break
#         else:
#             s=j
#     if s!=0:
#         while x%s==0 and c<=x:
#             c=c*s
#             s1=s1+str(s)+"X"
#             x=x//s
#
# print(s1[:-1])


# k=[]
# for i in range(int(input())):
#     n,a,b=map(int,input().split())
#     p=list(range(1,n+1))
#     l=[ j for j in p if j<a and j<b]
#     l.append(b)
#     r=[j  for j in p if j>a and j>b]
#     p=[x for x in p if x>min(a,b) and x<max(a,b)]
#     r.append(a)
#     print(l,r)
#     print(p)
#     for x in range(n//2):
#         if len(r)<n//2:
#             if len(p)!=0 and max(p)>a:
#                 r.append(max(p))
#         elif len(l)<n//2:
#             if len(p)!=0 and min(p)<b:
#                 l.append(min(p))
#         else:
#             break
#
#
#     print(l,r)
#
#
# for t in k:
#     print(t)