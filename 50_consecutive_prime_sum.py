
# coding: utf-8

# In[12]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def next_prime(n):
    if n==2: return 3
    if n%2==0: n-=1
    while not isprime(n+2):
        n+=2
    return n+2

def before_prime(n):
    if n==2: return 3
    if n%2==0: n-=1
    while not isprime(n+2):
        n+=2
    return n+2


print next_prime(11)

lp =2
hp=3

primes =[]
for x in range(2,1000000):
    if isprime(x):
        primes.append(x)


    
    


# In[35]:


maxsumpr =0
maxcount=0
prime = 0
for  prime in reversed(primes):
    sump=0
    counter = 0
    hpi = 0
    for hpi,iprime in enumerate(primes):
        sump+=iprime
        counter+=1
        if sump>=prime:
            break 
    lpi=0
    if counter < maxcount:
        break
    while sump !=prime :
        if sump == prime:
            break
        if sump >prime:
            sump= sump-primes[lpi]
            lpi+=1
            counter-=1
        elif sump < prime:
            hpi+=1
            counter+=1
            sump = sump+primes[hpi]
            
    if sump==prime and counter >maxcount:
        maxcount = counter
         
        
print maxcount, prime


# In[ ]:



