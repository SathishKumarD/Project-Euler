
# coding: utf-8

# In[34]:

def factors(n):
    factors=[]  
    d=1
    while n>1:
        if n%d==0:
            factors.append(d)
            if n/d != d and d!=1:
                factors.append(n/d)
        d=d+1
        if d*d>n:
            break;
    return factors

amicables =[]
sumfactors={}
for x in range(1,10000):
    sumfactors[x]=sum(factors(x))
#print sumfactors

for key,value in sumfactors.iteritems():
    if value in sumfactors.keys() and key!=value and sumfactors[value] == key and key not  in amicables:
        amicables.append(key)
        amicables.append(value)
        
        
sum(amicables)



# In[ ]:



