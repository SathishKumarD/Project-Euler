
# coding: utf-8

# In[19]:

import datetime
counter = 0
start =  datetime.datetime.now()
for x in xrange(1000):
    if x%10==0:
        continue
    r = x+int(str(x)[::-1])
    while r%10%2:
        r=r/10
    if not r:
        counter+=1
print counter
end =  datetime.datetime.now()
print end-start
        


# In[ ]:




# In[ ]:



