
# coding: utf-8

# In[9]:

sumd=0
for x in xrange(2,200000,1):
    tot=0
    for d in str(x):
        tot+=int(d)**5
    if tot==x:
        sumd+= x
        print x
print sumd        


# In[ ]:



