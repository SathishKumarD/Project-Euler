
# coding: utf-8

# In[3]:

def isprime(n):
    if n<=1:
        return False
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def tprime(n):
    sn= str(n)
    tp=True
    tp = isprime(n)
    if tp:
        for idx, c in enumerate(sn):             
            if sn[0:idx+1]:
                tp= tp and  isprime(int(sn[0:idx+1]))
            if sn[idx+1:]:
                tp = tp and isprime(int(sn[idx+1:]))
    return tp

n=11
sumtp=0
for x in range(11,1000000):
    if tprime(x):
        #print x
        n-=1
        sumtp+=x
        if not n:
            break
    

print sumtp;


# In[ ]:



