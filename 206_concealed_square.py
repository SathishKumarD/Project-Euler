
# coding: utf-8

# In[63]:

found = False
for m in range(10005678,14085679):
    for d in [30,70]:
        ans = ((m*100+d)**2)/100
        for n in range(1,9):
            ans= ans/(100)
            if ans%10 != 9-n:
                break
            if n==8:
                print m,k
                found = True
        if found:
            break
    if found:
        break   

print 'done'


# In[ ]:




# In[ ]:




# In[ ]:



