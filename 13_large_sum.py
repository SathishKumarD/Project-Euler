
# coding: utf-8

# In[9]:

lines = open('L:\\p13.txt').read().splitlines()

sumd =0
for line in lines:
    sumd= sumd+int(line)
print str(sumd)[0:10]
    


# In[ ]:



