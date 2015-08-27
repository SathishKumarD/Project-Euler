
# coding: utf-8

# In[16]:

def getPandigitals(ostart,oend,istart,iend):
    p=set()
    for d1 in xrange(ostart,oend):
        for d4 in xrange(istart,iend):
            k= str(d1)+str(d4)+str(d1*d4)
            b=[c for c in k]
            b.sort()
            if "".join(b)=="123456789":
                print d1,d4,d1*d4
                p.add(d1*d4)
    return p          
p1= getPandigitals(1,9,1234,9999)
p2= getPandigitals(10,99,100,999)

print p2
print sum(p1)+sum(p2)
        


# In[ ]:



