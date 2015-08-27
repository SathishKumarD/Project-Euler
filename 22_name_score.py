
# coding: utf-8

# In[9]:

import urllib2
response = urllib2.urlopen('https://projecteuler.net/project/resources/p022_names.txt')
html = response.read()
names =html.replace("\"","").split(',')
names.sort()


def getNameScore(name):
    score=0
    for c in name:
        score+= (ord(c)-64)
    return score

totalscore=0
for  idx,name in enumerate(names):
    totalscore+= (idx+1)*getNameScore(name)
    
print totalscore
    
    


# In[ ]:



