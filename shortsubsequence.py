from pip._vendor.distlib.compat import raw_input

n=int(raw_input())
s="codeforces"
s=s+(n-1)*"s"
print(s)
'''s1=list(s)
s2=['s']
i=0
s2=""
while i<n-1:
    s1.extend("s")
    i+=1

for x in s1:
    s2=s2+x
print(s2)'''