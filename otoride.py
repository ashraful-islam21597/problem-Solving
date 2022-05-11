from collections import Counter

ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7,
            1, 1, 2, 4, 7, 8, 9, 6, 6, 6]

# printing initial ini_list
print ("initial list", str(ini_list))

# sorting on bais of frequency of elements
result = [item for items, c in Counter(ini_list).most_common()
          for item in [items] * c]

# printing final result
print("final list", str(result))
print(list(set(result)))
k=[]
k1=list(set(result))
for j in list(set(result)):
    k.append(result.count(j))
print(k)
for i in range(len(k)):
    print(k.index(min(k))+1)
    k.remove((min(k)))
print(k)