# def slice(x,k):
#     if (len(x))%2!=0:
#         mid=(len(x)//2)
#         mid=mid+1
#         x1=x[:mid]
#         print(sum(x1))
#         if sum(x1)<k:
#             return slice(x[mid:],k)
#         else:
#             return mid
#     else:
#         mid=(len(x)//2)
#         if sum(x[0:mid])<k:
#             return slice(x[mid:],k)
#         else:
#             return mid
# x=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#    ]
# print(slice(x,2925))
#
k1=[]
for i in range(int(input())):
    mid=0
    s=0
    n , l, r, k = map(int,input().split())
    a=[int(j) for j in input().split()]
    a.sort()
    sum=0
    for t in a:
        if t <= r and t>=l:
            sum=sum+t
            if sum<=k:
                s=s+1
            else:
                break

    k1.append(s)
for k2 in k1:
    print(k2)




    # print(len(min_a))
    # if (len(min_a))%2!=0:
    #     mid=(len(min_a)//2)+1
    # else:
    #     mid=(len(min_a)//2)
    # z=min_a[:mid]
    # print(min_a)
    # print(z)

