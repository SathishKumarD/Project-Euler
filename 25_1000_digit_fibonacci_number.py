
# coding: utf-8

# In[1]:

a,b=0,1
counter =2
while len(str(b))<1000:  
    if(len(str(a+b)))==1000:
        print counter, a+b
        break;
        
    a,b=b,a+b
    counter+=1


# In[ ]:



