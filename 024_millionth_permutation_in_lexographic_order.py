
# coding: utf-8

# In[26]:

# Find the millionths permutation

combination = 1000000-1
digits = [0,1,2,3,4,5,6,7,8,9]
ans = []
def factorial(n):
    f = 1
    for x in range(1,n+1):
        f*=x
    return f
        
total = 0

for x in range(9,-1,-1):
    counter = 0
    fact =factorial(x)
    for coeff in range(0,11):
        if total+coeff*fact > combination:
            total+= (coeff-1)*fact
            counter = coeff-1
            break
    ans.append(digits[counter])
    del digits[counter]

print ans
 
    
    


# In[ ]:



