
# coding: utf-8

# In[2]:

filename='L:\\p18.txt'
lines = [line.rstrip('\n').split(' ') for line in open(filename)][::-1]


np = []

for idx,line in enumerate(lines):
    if idx == len(lines)-1:
        break
    nextline = lines[idx+1]
    if np:
        line=np
        np=[]
    for idx2,num in enumerate(nextline):
        np.append(max(int(num)+int(line[idx2]) ,int(num)+int(line[idx2+1])))
    
print np[0]   
        


# In[ ]:



