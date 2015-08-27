
# coding: utf-8

# In[5]:

import sys

p={}
for n in range(1,10000):
    p[n*(3*n-1)/2]=True

mind= sys.maxint
for j in p.keys():
    for k in p.keys():
        d= abs(j-k)
        if d in p and d in p and j+k in p:
            print j,k,p[d],p[j+k]
            mind = d if d< mind else mind
print mind

            
    


# In[ ]:



