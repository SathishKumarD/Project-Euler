
a=[]
a.append( [n*(n+1)/2 for n in range(150) if n*(n+1)/2 >=1000 and n*(n+1)/2 <10000 ])
a.append( [n*n for n in range(150) if n*n >=1000 and n*n <10000 and n*n%100>=10 and (n*n/100)*100>=10])
a.append( [n*(3*n-1)/2 for n in range(150) if n*(3*n-1)/2 >=1000 and n*(3*n-1)/2 <10000])
a.append([n*(2*n-1) for n in range(150) if n*(2*n-1) >=1000 and n*(2*n-1) <10000])
a.append( [n*(5*n-3)/2 for n in range(150) if n*(5*n-3)/2 >=1000 and n*(5*n-3)/2 <10000])
a.append( [n*(3*n -2) for n in range(150) if n*(3*n -2) >=1000 and n*(3*n -2) <10000])

from collections import OrderedDict
soln=OrderedDict()
seq=[]

def get_seq(num):
    for i in range(6):
        if i not in seq:
            seq.append(i)
            for index,x in enumerate(a[i]):
                if index>=0:
                    if num%100 == ((x/100)*100)/100 and num!=x:
                        soln[i]= x
                        first_item=next(soln.iteritems())[1]
                        if len(soln)==6 and ((first_item/100)*100)/100 == x%100:
                            print soln,sum(soln.values())
                            return True
                            break
                        else:
                            get_seq(x)
            delind =  seq.pop()
            if delind in soln:
                del soln[delind]
            

for x in a[0]:
    seq=[]
    seq.append(0) 
    soln=OrderedDict()
    soln[0]=x
    if get_seq(x):
        break
