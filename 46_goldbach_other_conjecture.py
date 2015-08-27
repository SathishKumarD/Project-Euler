
# coding: utf-8

# In[14]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def getMaxPrimesBelow(n):
    for x in range(n,1,-1):
        if isprime(x):
            yield x



def getConjecturefailure():
    for x in range(1,10000,2):
        if not isprime(x):
            found = False
            for s in range(1,x/2):
                primeGenerator = getMaxPrimesBelow(x)
                for p in primeGenerator:
                    if x == p+2*s*s:
                        found=True
                        break
                if found: break
            if not found:
                print x
                return x
                        

                
print getConjecturefailure()          
          
                
            
            


# In[ ]:



