
import numpy as np

def isprime(n):
    if n<0:
        return False
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def get_primes_under(n):
    primes = []
    for x in xrange(2,n):
        if isprime(x):
            primes.append(x)

    return primes

counter=0

def prime_factors(n):
    factors={}
    primes =get_primes_under(n+1)
    #print primes
    
    while n!=1:
        for p in primes:
            #print p
            while n%p==0:
                #print n
                if p in factors:
                    factors[p]+=1
                else:
                    factors[p]=1
                n=n/p
            if n==1:
                break
    return factors


def prime_factors_count(n):
    f=0
    primes =get_primes_under(n/2)
    if isprime(n):
        primes.append(n)
    for p in primes:
        if n%p==0:
            f+=1
        if f >4:
            break
    return f       




cc=0

cp=[]
for x in range(10000,100000):
    if prime_factors_count(x) == 4: 
        cp.append(x)
        cc+=1
        if cc==4:
            print 'yay',cp
            break
    else:
        cp=[]
        cc=0
            
    
print 'Done'       
    


print prime_factors(238203)
print prime_factors(238204)
print prime_factors(238205)
print prime_factors(238206)

print prime_factors_count(7*3)
print get_primes_under(22)




