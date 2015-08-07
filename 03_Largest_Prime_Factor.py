
# coding: utf-8

# In[ ]:

def getLargestPrimeFactor(n):
    factors=[]
    
    d=2
    while n>1:
        if n%d==0:
            factors.append(d)
            n=n/d
        d=d+1
        if d*d>n:
            factors.append(n)
            break;
    return factors

print max(getLargestPrimeFactor(600851475143))

        
        


# In[ ]:



