
# coding: utf-8

# In[5]:

a= 0
b = 1
summ=0;

for x in xrange(10000):
    c = a+b;
    if c%2==0:
        summ +=c
    if( c >= 4000000):
        break;
    #print c;
    a=b;
    b=c;
print summ


# In[ ]:



