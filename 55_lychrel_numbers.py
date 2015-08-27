
# coding: utf-8

# In[4]:

lych_counter=0
for x in range(10000):
    a=str(x)
    lych = True
    for i in range(50):
        a = str(int(a)+ int(a[::-1]))
        if a == a[::-1]:
            #print x,i,a
            lych = False
            break
    if  lych:
        lych_counter+=1
print lych_counter
    
        
    


# In[ ]:



