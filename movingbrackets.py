from pip._vendor.distlib.compat import raw_input
l=[]
i=0
for i in range(int(raw_input())):
    s1=int(raw_input())
    s=raw_input()
    st=""
    for k in s:
        s2=s.split("()")
        s=st.join(s2)
    l.append(s.count("("))

for j in l:
    print(j)