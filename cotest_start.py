def  sum_of_digit(n):
    if n%2!=0:
        x=n//2
        sum=x*(n+1)+(x+1)
    else:
        x=n//2
        sum=x*(n+1)
    return sum
k=[]
for i in range(int(input())):
    n,x,t=map(int,input().split())
    if t//x==n:
        k.append(sum_of_digit(n-1))
    elif (t//x)>n:
        k.append(sum_of_digit(n-1))
    else:
        a=sum_of_digit(t//x)
        f=a+(((n)-(t//x)-1)*(t//x))
        k.append(f)
for i in k:
    print(i)


