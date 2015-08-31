
# coding: utf-8

# In[9]:

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a;
def lcm(a,b):
    return (a*b)/gcd(a,b)

den_product =1
num_prod = 1
for x in range(1,10):
    for i in range(1,10):
        for y in range(10):
            if 9*x*y+i*y==10*x*i and 10*x+i !=10*i+y:
                #print 10*x+i,'/',10*i+y,x,y
                num_prod*=x
                den_product*=y
                
print lcm(num_prod ,den_product)/gcd(num_prod ,den_product)




# In[ ]:



