
# coding: utf-8

# In[1]:

cp =0
mp =0
for p in range(1,1000):
    r=[]
    for a in range(2,p-1):
        c = (1.0*a*a + (p - a)**2)/(2*(p-a))
        if int(c)==c and a>0 and c>0 and p-a-c >0:
            #print a,p-a-c,c,p
            r.append({'a':a,'b':p-a-c,'c':c})
            
    if len(r) > cp:
        cp=len(r)
        mp = p
print mp,cp      
    


# In[ ]:



