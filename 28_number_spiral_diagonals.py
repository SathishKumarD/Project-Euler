
# coding: utf-8

# In[13]:

diff =2
starter =1
sumdiag=1
for x in xrange(3,1002,2):
    sumdiag +=sum(n for n in range(starter+diff,starter+diff*5,diff))
    starter = starter+diff*4
    diff=diff+2
print sumdiag


# In[ ]:



