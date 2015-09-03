
# coding: utf-8

# In[5]:

pn=7
pd=5
counter =0
for n in range(2,1000):
    n= 2*pd+pn
    d = pn+pd
    if len(str(n))>len(str(d)):
        counter+=1
    pn,pd=n,d
        
print counter
    


# In[ ]:



