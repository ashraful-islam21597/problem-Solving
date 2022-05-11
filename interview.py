# address = input()
# address_list = address.split(" ") # split string by space and convert into list
# new_address = []
# i = 0
# s = ""
# while i < len(address_list):
#     if s != address_list[i]:
#         if s.capitalize() == str(address_list[i]).capitalize(): #differ capitalize and and non Capitalize
#             new_address.pop()
#             new_address.append(str(address_list[i]).capitalize())
#             s = str(address_list).capitalize()
#         else:
#             new_address.append(address_list[i])
#             s = address_list[i]
#     i = i + 1
# new_address_string = ' '.join(i for i in new_address)
# print(new_address_string)

# import math
# k = []
#
# for i in range(int(input())):
#     T = int(input())
#     powers = int(math.log(T, 2))
#     sum_of_turn = T * ((T + 1) / 2)
#     sum_of_power_two = 0
#     for i in range(powers + 1):
#         sum_of_power_two = sum_of_power_two + 2 ** i
#     k.append(int(sum_of_turn - 2 * sum_of_power_two))
#
# for t in k: #output
#     print(t)

# 1. Find Prime Factor

# import math
# def prime_factor(x):
#     #x = int(input())
#     divisors = [i for i in range(2, (x // 2) + 1) if x % i == 0]  # divisor of x from 2 to s/2
#
#     prime_divisors = []
#
#     for divisor in divisors:  # prime divisor of x
#         prime = divisor
#         y = math.sqrt(divisor) + 1  # square root of each divisor
#         for i in range(2, int(y)):
#             if divisor % i == 0:
#                 prime = 0
#                 break
#             else:
#                 prime = divisor
#         if prime != 0:
#             prime_divisors.append(prime)
#
#     if prime_divisors == []:
#         prime_divisors.append(x)
#
#     string = str(x) + " = "
#
#     for factor in prime_divisors:  # to generate a string by the prime factors
#         while x % factor == 0:
#             string = string + str(factor) + " X "
#             x = x // factor
#     return (string[:-2])
# for i in range(0,5):
#     print(prime_factor(int(input())))
#
# #2.The Spoiled Siblings
#
# import math
# k = []
#
# for i in range(int(input())):
#     T = int(input())
#     powers = int(math.log(T, 2))
#     sum_of_turn = T * ((T + 1) / 2)
#     sum_of_power_two = 0
#     for i in range(powers + 1):
#         sum_of_power_two = sum_of_power_two + 2 ** i
#     k.append(int(sum_of_turn - 2 * sum_of_power_two))
#
# for t in k: #output
#     print(t)
#
# #3.Dups Remove
#
# address = input()
# address_list = address.split(" ") # split string by space and convert into list
# new_address = []
# i = 0
# s = ""
# while i < len(address_list):
#     if s != address_list[i]:
#         if s.capitalize() == str(address_list[i]).capitalize(): #differ capitalize and and non Capitalize
#             new_address.pop()
#             new_address.append(str(address_list[i]).capitalize())
#             s = str(address_list).capitalize()
#         else:
#             new_address.append(address_list[i])
#             s = address_list[i]
#     i = i + 1
# new_address_string = ' '.join(i for i in new_address)
# print(new_address_string)
class Solution(object):
    def longestPalindrome(self,s):
        c=0
        a=0
        l=[]
        s3=""
        if s==s[::-1]:
            return s
        elif len(set(s))==len(s):
            return s[0]
        else:
            for i in s:
                t=0
                s1=list(s[::-1])

                if s.count(i)>1:
                    for j in range(s.count(i)-1):
                        z=s1.index(i)
                        p=s[c:(len(s1)-(z+1)+1)]

                        s1.pop((z))

                        if p==p[::-1]:
                            if len(s3)<len(p):

                                s3=p
                c+=1
            return s3
s=Solution()
print(s.longestPalindrome(input()))