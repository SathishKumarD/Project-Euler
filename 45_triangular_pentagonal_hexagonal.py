
# coding: utf-8

# In[7]:

T,P,H={},{},{}

for n in range(286,100000):
    T[n*(n+1)/2]=True

for n in range(166,100000):
    P[n*(3*n-1)/2]=True
    
for n in range(144,100000):
    H[n*(2*n-1)]=True

for t in T.keys():
    if t in P and t in H:
        print x,t
        break
print "none found"


# In[ ]:



