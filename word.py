from pip._vendor.distlib.compat import raw_input
s= raw_input()
i=0
j=0
for x in s:
    if x.islower():
        i+=1
    else:
        j+=1
if j>i:
    print(s.upper())
else:
    print(s.lower())