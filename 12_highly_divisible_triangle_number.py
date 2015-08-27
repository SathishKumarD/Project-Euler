
# coding: utf-8

# In[66]:

import math
def num_of_factors(n):
    f = 2
    for d in range(2,n):
        if d*d >n:
            break
        if n%d==0:
            f+= 1 if d*d==n else 2
    return f

prev=2
for x in range(100000):
    n=num_of_factors(x)
    if prev*n>500 and num_of_factors((x-1)*x/2) >500:
        print x-1,x,(x-1)*x/2
        break
    prev=n





# In[ ]:




# In[ ]:



