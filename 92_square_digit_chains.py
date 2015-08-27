
# coding: utf-8

# In[37]:

c=0
h={}
for n in range(2,10000000):
    b=n
    while True:
        sumd=0
        while n:
            sumd, n = sumd + (n % 10)**2, n / 10
        if sumd==89 or sumd in h:
            if b <=567:
                h[b]= True
            c+=1
            break
        if sumd == 1:
            break
        n=sumd
print c          


# In[ ]:




# In[ ]:



