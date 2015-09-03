
# coding: utf-8

# In[79]:

def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

primes = []
for x in range(3,10000):
    if isprime(x):
        primes.append(x)
        
def isprime_3(n):
    for d in primes:
        if d*d>n or n%d ==0 :
            break
    return n<d*d



# In[ ]:



ispair = True
found=False

for p1 in primes:
    ispair = True
    if found:break
    ps.append(p1)
    for p2 in primes:
        ispair = True
        if found:break
        ispair = p2 not in ps and isprime_3(int(str(p1)+str(p2))) and isprime_3(int(str(p2)+str(p1)))
        if ispair and not found :
            ps.append(p2)
            #print ps
            for p3 in primes:
                ispair = True
                if found:break
                for x in ps:
                    ispair = ispair and p3 not in ps  and isprime_3(int(str(x)+str(p3))) and isprime_3(int(str(p3)+str(x)))
                    #print ispair, str(x)+str(p3), isprime_3(int(str(x)+str(p3))),str(p3)+str(x), isprime_3(int(str(p3)+str(x)))
                if ispair and not found:
                    ispair = True
                    ps.append(p3)
                    #print ps
                    for p4 in primes:
                        ispair = True
                        if found:break
                        for y in ps:
                            ispair = ispair and p4 not in ps and isprime_3(int(str(y)+str(p4))) and isprime_3(int(str(p4)+str(y)))
                        if ispair and not found:
                            ps.append(p4)
                            #print ps
                            for p5 in primes:
                                ispair = True
                                for z in ps:
                                    ispair = ispair and p5 not in ps and isprime_3(int(str(z)+str(p5))) and isprime_3(int(str(p5)+str(z)))
                                if ispair:
                                    ps.append(p5)
                                    print ps,sum(ps)
                                    found = True
                                    break
                                        
                            del ps[-1]
                    del ps[-1]
            del ps[-1]
    del ps[-1]
    


# In[ ]:




# In[ ]:




# In[ ]:



