
# coding: utf-8

# In[20]:

import numpy as np

def isprime(n):
    if n<0:
        return False
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def get_primes_under(n):
    primes = []
    for x in xrange(2,n):
        if isprime(x):
            primes.append(x)
    return primes

counter=0

def prime_factors(n):
    factors={}
    primes =get_primes_under(n+1)
    #print primes
    while n!=1:
        for p in primes:
            #print p
            while n%p==0:
                #print n
                if p in factors:
                    factors[p]+=1
                else:
                    factors[p]=1
                n=n/p
            if n==1:
                break
    return factors

            
print prime_factors(100)        

listF = []
for a in range(2,101):
    for b in range(2,101):
        factors = prime_factors(a)
        for key,value in factors.iteritems():
            factors[key]*=b
        #print a,b, factors   
        listF.append(factors)
        
list_of_unique_dicts=list(np.unique(np.array(listF)))
print len(list_of_unique_dicts)


# In[ ]:




# In[ ]:



