
# coding: utf-8

# In[34]:

def nth_prime(n):
    if n==1: return 2
    n-=1
    i=3
    while n:
        if isprime(i):
            n-=1
            if not n:
                break
        i+=2
    return i
            
def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

print  nth_prime(5)          
        


# In[ ]:



