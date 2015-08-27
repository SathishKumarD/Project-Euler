
# coding: utf-8

# In[60]:

num={}

num[1]="one"
num[2]="two"
num[3]="three"
num[4]="four"
num[5]="five"
num[6]="six"
num[7]="seven"
num[8]="eight"
num[9]="nine"
num[10]="ten"
num[11]="eleven"
num[12]="twelve"
num[13]="thirteen"
num[14]="fourteen"
num[15]="fifteen"
num[16]="sixteen"
num[17]="seventeen"
num[18]="eighteen"
num[19]="nineteen"
num[20]="twenty"
num[30]="thirty"
num[40]="forty"
num[50]="fifty"
num[60]="sixty"
num[70]="seventy"
num[80]="eighty"
num[90]="ninety"
num[100]="hundred"
num[1000]="thousand"

def printNum(n):
    stri=''
    if(n==0):
        return ""
    if (n >=1 and n<=20):
        return num[n]
    d=len(str(n))-1
    if d>=2: 
        stri+=num[n/(10**d)]+ num[10**d]
        if n!=(n/(10**d))*10**d: stri+="and" 
    else: 
        stri+=num[(n/(10**d))*10**d]
    return stri+printNum(n%(10**d))

print sum(len(printNum(x)) for x in xrange(1,1001))




# In[ ]:



