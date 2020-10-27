from pip._vendor.distlib.compat import raw_input

s=raw_input()
k=len(s)
if s[1:].isupper():
    print( s[0].swapcase()+s[1:].lower())
elif k==1 :
    print(s.swapcase())
else:
    print(s)

'''k=s[0].islower()+s[1:]
#print(s[0].lower()+s[1:].upper())
#if s[0:].isupper() or (s[0].islower()+s[1:].isupper()):

#print(s[0]+s[1:].casefold())
if s.isupper():
    print(s.lower())
elif k:
     print(s[0].upper()+s[1:].lower())
else:
    print(s)'''