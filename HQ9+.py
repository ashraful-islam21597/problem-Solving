
from pip._vendor.distlib.compat import raw_input

import re
text=str(raw_input())
l=['H','Q','9']
s=""
for x in l:
    n=re.findall(x,text)
    if n:
        s="YES"
        break
    else:
        s="NO"

print(s)
