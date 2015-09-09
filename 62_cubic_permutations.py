import math

def get_digits(n):
    p1digits =[0 for x in xrange(10)]
    while n:
        rem = n%10
        p1digits[rem]+=1
        n/=10
    return p1digits

def get_cube_ranges(maxdigits):
    cube_ranges = []
    for d in range(3,maxdigits):
        minval = math.pow( 10**d,1.0/3.0)
        maxval = math.pow( 10**(d+1), 1.0/3)
        cube_ranges.append( [int(math.ceil(minval)),int(math.floor(maxval))])
    return cube_ranges
        
        

def get_cubic_permutations():
    
    cube_ranges = get_cube_ranges(20)
    for cube_range in cube_ranges:
        cubes = []
        for x in xrange(cube_range[0],cube_range[1]):
            cubes.append(x**3)
        for p1 in cubes:
            p1digits = get_digits(p1)
            for p2 in cubes:
                if p1== p2:
                    continue
                p2digits = get_digits(p2)
                if p1digits == p2digits:
                    for p3 in cubes:
                        if p3 == p2 or p3==p1:
                            continue
                        p3digits = get_digits(p3)
                        if p3digits == p2digits:
                            for p4 in cubes:
                                if p4 == p1 or p4==p2 or p4== p3:
                                    continue
                                p4digits = get_digits(p4)
                                if p4digits == p3digits:
                                    for p5 in cubes:
                                        if p5 == p1 or p5==p2 or p5== p3 or p5== p4:
                                            continue
                                        p5digits = get_digits(p5)
                                        if p5digits == p4digits:
                                            return p1
                                    
print get_cubic_permutations()

