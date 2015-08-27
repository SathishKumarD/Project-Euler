
# coding: utf-8

# In[5]:

counter = 0
for x in range(1,100):
    for p in range(1,100):
        if len(str(x**p))==p:
            counter+=1
            #print x,p
print counter 


# In[ ]:



