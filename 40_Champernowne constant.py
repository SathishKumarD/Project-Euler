
# coding: utf-8

# In[1]:

d=''
for x in range(1,1000000):
    d+=str(x)
    if len(d)>=1000000:
        break
prod=1;
for i in range(7):
    prod*=int(d[10**i-1])
print prod
    
        
    


# In[ ]:



