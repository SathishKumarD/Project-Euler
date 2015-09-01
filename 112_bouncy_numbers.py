
# coding: utf-8

# In[14]:

bcounter = 0
for n in range(1,10000000):
    x=n
    prem = x%10
    x=x/10
    isDown,isUp = False,False
    while x:
        rem = x%10
        if rem >prem:
            isUp = True
        elif rem < prem:
            isDown=True
        prem = rem
        x/=10
        
        if isUp and isDown:
            bcounter+=1
            break
    int_percentage = 100*bcounter/n
    real_percentage = (1.0* 100.0*bcounter)/n
    if int_percentage == real_percentage and bcounter!=0 and int_percentage==99:
        print int_percentage, '%',n


# In[ ]:




# In[ ]:



