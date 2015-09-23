
# coding: utf-8

# In[6]:

def total_possible_combinations(denominations,total):
    ans=[ [1 for i in range(total+1)] for j in denominations] # fill the result matrix with all 1
    for i, den in enumerate(denominations): # iterate through all the denominations
        for j in range(2,total+1): # iterate from 2 to total
            if j <den and i >0:
                ans[i][j] = ans[i-1][j]
            if j >=den and i>0:
                ans[i][j] = ans[i-1][j]+ ans[i][j-den]
    return ans[len(denominations)-1][total]


if __name__ == '__main__':
    denominations=[x for x in range(1,100) ]
    total = 100
    print(total_possible_combinations(denominations,total))


# In[ ]:




# In[ ]:




# In[ ]:



