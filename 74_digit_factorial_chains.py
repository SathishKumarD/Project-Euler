
# coding: utf-8

# In[27]:

def get_sum_dig(num):
    h[num] = True
    sumd=0
    while num:
        fact=1
        for x in range(1,num%10 +1):
            fact *=x
        sumd+=fact
        num/=10
    if sumd not in h:
        h[sumd] = True
        get_sum_dig(sumd)
        return len(h)

counter = 0
for x in range(2,1000000):
    h={}
    if get_sum_dig(x)==60:
        counter+=1
print counter

        
    


# In[ ]:



