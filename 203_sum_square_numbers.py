
# coding: utf-8

# In[43]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

# calculate first 100 prime squares
squares = []
for x in range(2,100):
    if isprime(x):
        squares.append(x*x)



# generate pascal triangle with 51 rows
u = set()
u.add(1)
prev = [1,1]
for x in range(3,52):
    now = [1]
    for idx,y in enumerate(prev[:len(prev)-1]):
        u.add( y+prev[idx+1])
        now.append(y+prev[idx+1])
    now.append(1)
    prev = now

# check if it is square free
sump = 0
for x in u:
    issf = False
    for s in squares:
        if x%s==0 :
            issf = True
            break
    if not issf:
        sump+=x
        
print sump
        
        
        


# In[ ]:




# In[ ]:



