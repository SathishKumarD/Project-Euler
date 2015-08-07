
# coding: utf-8

# In[ ]:




# In[10]:

def sumMultiple3or5(N):
    n5 = int(N/5)
    n15= int(N/15)
    n3= int(N/3)
    return 3* n3*(n3+1)/2 + 5* n5*(n5+1)/2- 15* n15*(n15+1)/2


print sumMultiple3or5(999)


# In[ ]:



