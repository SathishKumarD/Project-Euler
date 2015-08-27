
# coding: utf-8

# In[9]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

primes = 0
diff =2
starter =1
totalelements = starter
sumdiag=1
for x in xrange(3,100002,2):
    a =[n for n in range(starter+diff,starter+diff*5,diff)]
    totalelements+=len(a)
    
    for p in a:
        if isprime(p):
            primes +=1
    if 1.0*primes/totalelements <0.1:
        print x,primes,totalelements
        break
    
    starter = starter+diff*4
    diff=diff+2


# In[ ]:



