
def is_n_digit_same(number,n):
    snum = str(number)
    for d in snum:
        if snum.count(d)>=n:
            return True,d
    return False,0
        
        
def isprime(n):
    d=2
    while n>d*d and not n%d ==0 :
        d+=1
    return n<d*d

def get_min_no_of_repititive_digits(n_prime):
    for no_of_digits in range(1,10):
        for sum_of_other_digits in range(30):
            count = 0
            for digit in range(10):
                if (no_of_digits*digit+sum_of_other_digits)%3!=0:
                    count+=1
                if count == n_prime:
                    return no_of_digits
                    break

no_of_repititive_digits =  get_min_no_of_repititive_digits(8)


def get_min_prime_digit_replacement():
    for x in range(3,1000000,2):
        isn_dig,digit = is_n_digit_same(x,no_of_repititive_digits)
        if  isn_dig and isprime(x):
            counter = 0
            for d in range(10):
                sx= str(x)
                inum = int(sx.replace(str(digit),str(d)))
                if len(str(inum)) < len(str(x)):
                    continue
                if isprime(inum):
                    counter+=1
                if counter == 8:
                    return x
                
print get_min_prime_digit_replacement()
