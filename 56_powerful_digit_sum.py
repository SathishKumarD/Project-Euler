
# coding: utf-8

# In[1]:

maxsum = 0
for a in range(100):
    for b in range(100):
        sumd=0
        for c in str(a**b):
            sumd+= int(c)
        maxsum = sumd if maxsum < sumd else maxsum
print maxsum


# In[ ]:



