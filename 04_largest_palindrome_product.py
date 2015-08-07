
# coding: utf-8

# In[17]:


def largestPalindromeFromProduct(d):
    n1=d;
    maxpalin =0
    while n1>=100:
        n2=d
        while n2>=100:
            res = str(n1*n2)
            #print res,res[::-1],n1,n2
            if res[::-1] == res:
                maxpalin = int(res) if int(res)>maxpalin else maxpalin
            n2-=1
        n1-=1
    return maxpalin    
print largestPalindromeFromProduct(999)
    


# # 
