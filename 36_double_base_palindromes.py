
# coding: utf-8

# In[1]:

def binpalin(n):
    b=''
    while n:
        b=b+str(n%2)
        n/=2
    return (b[::-1] == b)
    
palin_sum=0

for x in range(1,1000000):
    xs= str(x)
    if xs==xs[::-1] and binpalin(x):
        #print x
        palin_sum+=x
print 'sum',palin_sum
        
        
    
        
    


# In[ ]:



