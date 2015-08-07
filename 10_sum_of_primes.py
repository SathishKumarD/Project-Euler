
# coding: utf-8

# In[7]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

print sum( x if isprime(x) else 0 for x in range(2,2000000))
    


# In[ ]:

142913828922

