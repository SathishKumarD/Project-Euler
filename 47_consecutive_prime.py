
# coding: utf-8

# In[6]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

primes =[]
for x in range(2,1000000):
    if isprime(x):
        primes.append(x)


# In[20]:

consec = 0
FACTORS = 4
for x in range(2,1000000): 
    n_factors = 0
    for f in primes:
        if x%f == 0: 
            n_factors+=1
        if f >=x/2 or n_factors >FACTORS:
            break
    if n_factors == FACTORS:
        consec+=1
    else:
        consec=0
    if consec == FACTORS:
        print x-3,x-2,x-1,x
        break
         


# In[ ]:




# In[ ]:



