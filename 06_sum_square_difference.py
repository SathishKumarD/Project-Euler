
# coding: utf-8

# In[8]:

def sum_of_sqr_minus_sqr_of_sum(n):
    sum_of_sqr = n*(n+1)*(2*n+1)/6
    sqr_of_sum = ((n*(n+1))**2)/4
    return  sqr_of_sum -sum_of_sqr


print sum_of_sqr_minus_sqr_of_sum(100)


# In[ ]:



