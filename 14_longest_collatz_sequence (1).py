
# coding: utf-8

# In[27]:

def collatz(n):
    if n== 1: return 1
    if n%2==0: return 1+collatz(n/2)
    return 1+ collatz(3*n+1)

mcollatz,num=0,0

for x in xrange(899999,799999,-1):
    c= collatz(x)
    if mcollatz < c:
        mcollatz,num = c,x 
print "ans", mcollatz,num     


# In[ ]:



