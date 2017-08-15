L1=['Hello','world',18,'Apple',None]
L2=[]
for i in range(len(L1)-1):
    #print(i)
    #print(L1[i])
    if not isinstance(L1[i],str):
       L1.pop(i)
L2=[s.lower() for s in L1]
#print(list(range(len(L1))))
print(L2)