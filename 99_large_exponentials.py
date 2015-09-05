
import math

exp_list = open('p099_base_exp.txt').read().split('\n')
first = [int(x) for x in exp_list[0].split(',')]
maxexp = first[1]*math.log(first[0])
maxcounter = 1
counter = 0
for exp in exp_list:
    counter += 1
    int_arr = [int(x) for x in exp.split(',')]
    result = int_arr[1]*math.log(int_arr[0])
    if result > maxexp:
        maxexp = result
        maxcounter = counter

print maxcounter
