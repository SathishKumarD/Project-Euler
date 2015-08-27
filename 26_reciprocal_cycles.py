
# coding: utf-8

# In[ ]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def getPeriod(n):
    x=1
    while True:
        if 10**x %n==1:
            return x
        x+=1
print getPeriod(211)


periods={}
maxd,maxp=0,0
for x in range(1000,1,-1):
    if isprime(x):
        #print x
        p =getPeriod(x)
        periods[x]=p
        maxd = x if p>maxp else maxd
        maxp = p if p>maxp else maxp
        print x, p,maxd,maxp
print periods 


# In[ ]:



