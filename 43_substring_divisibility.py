
# coding: utf-8

# In[13]:

from itertools import permutations
perms = [''.join(p) for p in permutations('0123456789')]
sump =0
for snum in perms:
    
    isdiv= True
    isdiv = isdiv and int(snum[1:4])%2 ==0
    isdiv = isdiv and int(snum[2:5])%3==0
    isdiv = isdiv and int(snum[3:6])%5==0
    isdiv = isdiv and int(snum[4:7])%7==0
    isdiv = isdiv and int(snum[5:8])%11==0
    isdiv = isdiv and int(snum[6:9])%13==0
    isdiv = isdiv and int(snum[7:10])%17==0
    if isdiv:
        sump+= int(snum)

print sump         


# In[ ]:




# In[ ]:



