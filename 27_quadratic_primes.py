
# coding: utf-8

# In[12]:

def isprime(n):
    if n<0:
        return False
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def getPrimecount(a,b):
    for x in xrange(1000):
        if not isprime(x*x+a*x+b):
            return x

print getPrimecount(-61,971)

p=[]
for x in range(-1000,1000):
    if isprime(abs(x)):
        p.append(x)
        
primes =[]
maxa,maxb=0,0
maxcount=0
for a in p:
    for b in p:
        pcount = getPrimecount(a,b)
        if pcount >maxcount:
            maxcount=pcount
            maxa,maxb=a,b
        primes.append({'a':a,'b':b,'primes':pcount})
print maxa,maxb,maxcount

print maxa*maxb


# In[ ]:



