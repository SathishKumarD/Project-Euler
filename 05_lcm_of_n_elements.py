
# coding: utf-8

# In[23]:

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a;
def lcm(a,b):
    return (a*b)/gcd(a,b)

def lcm_n(*args):
    return reduce(lcm, args)

print lcm_n(*range(1,20))


        


# In[ ]:




# In[ ]:



