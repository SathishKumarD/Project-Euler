import math
tnum,tden,maxint =0,0,0
for den in range(7,1000000):
    low =  int(math.floor(den*1.0*0.4285))
    high = int(math.ceil(den*1.0*0.4286))
    for num in range(low,high+1):
        val = num*1.0/den
        if maxint < val and val < 3.0/7 :
            maxint = val
            tnum,tden = num,den
print tnum