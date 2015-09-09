
pprev = 1
prev = 2
for i in range(3,102):
    if i%3==0 or i%3==2:
        p = prev + pprev
    else:
        p = 2*(i-1)*prev/3 + pprev
    pprev = prev
    prev = p
    if i==101:
        print sum( int(d) for d in str(p))
        break  



