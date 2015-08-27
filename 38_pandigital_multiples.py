
# coding: utf-8

# In[1]:

maxp = 0
for x in range(1,1000000):
    s=''
    pan= True
    for y in range(1,10):
        s+=str(x*y)
        if len("".join(set(s))) != len(s) or len(s) > 9 or '0' in s:
            pan = False
            break
        if len(s) == 9:
            pan= True
            break
    if pan:
        maxp = int(s) if int(s) > maxp else maxp
print maxp


# In[ ]:



