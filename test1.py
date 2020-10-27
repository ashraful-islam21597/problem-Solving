n=int(input())
i = 1
s=""
while i<=n :
  s=s+str(i)
  if len(s)==990:
      print(i)
      break
  i += 1
print(s)
print(len(s))