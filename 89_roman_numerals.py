
# coding: utf-8

# In[35]:

ralphabets={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

romans = open('p089_roman.txt').read().split('\n')

saved_chars=0
for roman in romans:
    num=0
    oroman= roman
    for idx, r in enumerate(roman):
        if idx < len(roman)-1 and ralphabets[r] <ralphabets[roman[idx+1]]:
            num-= 2*ralphabets[r]
        num+=ralphabets[r]
    
    decimal = num
    optNum=''
    for t in range(num/1000):
        optNum+= 'M'
    num=num%1000

    if num/100 == 4:
        optNum+='CD'
        
    elif num/100 == 9:
        optNum+='CM'
        
    else:
        if num >= 500:
            optNum+='D'
            num=num-500
        for c in range(num/100):
            optNum+='C'
                   
    num=num%100
    if num/10==4:
        optNum+='XL'
       
    elif num/10==9:
        optNum+='XC'
        
    else:
        if num >= 50:
            optNum+='L'
            num=num-50
    
        for c in range(num/10):
            optNum+='X'
                
    num = num%10
    
    if num==4:
        optNum+='IV'
       
    elif num==9:
        optNum+='IX'
        
    else:
        if num >= 5:
            optNum+='V'
            num=num-5

        for c in range(num):
            optNum+='I'
            
    #print oroman, decimal, optNum
    saved_chars+=len(oroman)-len(optNum)
    if len(oroman)-len(optNum)<0:
        print 'omg',oroman,optNum
    
print saved_chars
    
    
        
        
            
    



# In[ ]:



