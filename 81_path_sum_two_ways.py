import numpy as np
matrix = open('p081_matrix.txt').read()

lines =  matrix.split('\n')
lines = lines[0:len(lines)-1] # removing empty row at the end
rows = len(lines)
cols = len(lines[0].split(','))


# In[39]:

elements = np.array([ [int(m) for m in x.split(',')] for x in lines]).reshape(rows,cols)
distance = np.zeros(rows*cols).reshape(rows,cols)
dist = 0
for idx, x in enumerate(distance[0]):
    dist+=elements[0][idx]
    distance[0][idx] = dist

for iidx, i in enumerate( distance[1:]):
    for jidx, j in enumerate (i):
        if jidx == 0:
            distance[iidx+1][jidx]=  distance[iidx][jidx] +  elements[iidx+1][jidx]
        else:
            distance[iidx+1][jidx]=  min(distance[iidx][jidx] ,distance[iidx+1][jidx-1])+  elements[iidx+1][jidx]

print distance[rows-1][cols-1]