
# coding: utf-8

# In[25]:

''

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def allcomb(n):
    sn =str(n)
    comb=[]
    for idx,c in enumerate(sn):
        comb.append(c+sn[idx+1:] +sn[0:idx])
    #print comb
    return comb

cpcount=0        
for x in xrange(2,1000000):
    if isprime(x):
        combs = allcomb(x)
        cprime = True
        for comb in combs:
            if cprime:
                cprime =isprime(int(comb))
            else:
                #print comb
                break
        if cprime:
            #print 'cp',x
            cpcount+=1
print cpcount
                
        


# In[ ]:



