def gcd(a,b):
    while b:
        a,b=b,a%b
    return a;

import math

h={}
for den in range(2,12001):
    low =  int(math.floor(den*1.0*0.333))
    high = int(math.ceil(den*1.0*0.5))
    for num in range(low,high+1):
        val = num*1.0/den
        if val>1.0/3 and val < 0.5 :
            g = gcd(num,den)
            h[ str(num/g)+'_'+str(den/g)] = True
            
print len(h)
