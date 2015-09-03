
# coding: utf-8

# In[4]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

pmult=0
mult=1
for x in range(2,1000000):
    if isprime(x):
        pmult=mult
        mult*=x
        #print mult
        if mult > 1000000:
            print pmult
            break


# In[ ]:



