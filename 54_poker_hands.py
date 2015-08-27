
# coding: utf-8

# In[12]:

ptxt=''
with open ("L:\\p054_poker.txt", "r") as myfile:
    ptxt=myfile.read()
games = ptxt.split('\n')

cardval={'2':2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13, 'A':14}


# all cards of the same suite
def isflush(game):
    cards= game.strip().split(' ')
    suite= cards[0][1:]
    isSame = True
    for card in cards:
        isSame=  isSame and card[1:]== suite
    return isSame

# all cards are continuous
def is_straight(game):
    cards= game.strip().split(' ')
    vals= [cardval[card[0:1]] for card in cards]
    vals.sort()
    init = vals[0]
    isConsec = True
    for x in range(1,len(cards)):
        isConsec = isConsec and vals[x] ==vals[x-1]+1
    return isConsec

#gets the nth highest card
def getHighestCard(game,nth):
    cards= game.strip().split(' ')
    vals= [cardval[card[0:1]] for card in cards]
    vals.sort()
    return vals[len(cards)-nth]
   
#straight flush
def is_straight_flush(game):
    return isflush(game) and is_straight(game)
    
#royal flush    
def is_royal_flush_winner(game):
    return isflush(game) and is_straight(game) and getHighestCard(game,1) == 14


# n of a kind
def is_n_of_a_kind(game,n):
    valdict={}
    cards= game.strip().split(' ')
    for card in cards:
        v= cardval[card[0:1]]
        if v in valdict:
            valdict[v]+=1
        else:
            valdict[v]=1
    #print valdict
    for key,val in valdict.iteritems():
        if val== n:
            return True,key
    return False,0

# two pairs
def is_two_pairs(game):
    valdict={}
    cards= game.strip().split(' ')
    for card in cards:
        v= cardval[card[0:1]]
        if v in valdict:
            valdict[v]+=1
        else:
            valdict[v]=1
    filtered = [k for (k,v) in valdict.iteritems() if v==2 ]
    if len(filtered)==2:
        filtered.sort()
        return True,filtered[1],filtered[0]
    
    return False,0,0
 
# full house :Three of a kind and a pair
def is_full_house(game):
    valdict={}
    cards= game.strip().split(' ')
    for card in cards:
        v= cardval[card[0:1]]
        if v in valdict:
            valdict[v]+=1
        else:
            valdict[v]=1
    
    contains3,Contains2=False,False
    val3,val2=0,0
    for key,val in valdict.iteritems():
        if val== 3:
            contains3,val3=True,key
        if val==2:
            Contains2,val2 = True,key
    return contains3 and Contains2,val3,val2

# flush winner
def flush_winner(A,B):
    winner = 0
    a = isflush(A)
    b=  isflush(B)
    
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        ahigh = getHighestCard(A,1)
        bhigh = getHighestCard(B,1)
        winner = 1 if ahigh > bhigh else -1
    print str(winner)+' has the flush'
    return winner

#straight winner    
def straight_winner(A,B):
    winner = 0
    a = is_straight(A)
    b=  is_straight(B)
    
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        ahigh = getHighestCard(A,1)
        bhigh = getHighestCard(B,1)
        winner = 1 if ahigh > bhigh else -1
    print str(winner)+' has the straight '
    return winner    

# royal flush winner
def royal_flush_winner(A,B):
    winner = 0
    a = is_royal_flush_winner(A)
    b = is_royal_flush_winner(B)
    if a and not b:
        winner = 1
    elif not a and b :
        winner = -1
    print str(winner)+' got the royal flush'
    return winner

# straight flush winner
def straight_flush_winner(A,B):
    winner = 0
    a = is_straight_flush(A)
    b=  is_straight_flush(B)
    
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        ahigh = getHighestCard(A,1)
        bhigh = getHighestCard(B,1)
        winner = 1 if ahigh > bhigh else -1
        
    print str(winner)+' has the straight royal flush'
    return winner

# n of a kind
def n_of_a_kind_winner(A,B,n):
    winner = 0
    a, ahigh = is_n_of_a_kind(A,n)
    b, bhigh = is_n_of_a_kind(B,n)
    
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        if ahigh > bhigh:
            winner=1
        elif bhigh>ahigh:
            winner = -1
        else:
            winner =highest_card_winner(A,B)
    
    print str(winner)+' is the '+str(n)+' of a kind winner'
    return winner
    
# full house winner: three of a kind and pair        
def full_house_winner(A,B):
    winner = 0
    a, a3,a2 = is_full_house(A)
    b, b3,b2=  is_full_house(B)
    
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        if a3 > b3:
            winner=1
        elif b3>a3:
            winner = -1
        else:
            winner =highest_card_winner(A,B)
        
    print str(winner)+' is the full house winner'
    return winner

# two of a pair winner
def two_of_a_pair_winner(A,B):
    winner = None
    a,a1,a2=is_two_pairs(A)
    b,b1,b2= is_two_pairs(B)
    print a , a1, a2, b, b1, b2
    if a and not b :
        winner = 1
    elif not a and b :
        winner = -1
    elif a and b:
        if a1> b1:
            winner=1
        elif b1 > a1:
            winner = -1
        elif a2> b2:
            winner=-1
        elif b2> a2:
            winner = -1
        else:
            winner =highest_card_winner(A,B)
        
    print str(winner)+' is the full house winner'
    return winner
    
    
def highest_card_winner(A,B):
    winner = 0
    Acards= A.strip().split(' ')
    Avals= [cardval[card[0:1]] for card in Acards]
    Avals.sort(reverse=True)
    
    Bcards= B.strip().split(' ')
    Bvals= [cardval[card[0:1]] for card in Bcards]
    Bvals.sort(reverse=True)
    #print Avals, Bvals, len(Avals)
    for idx in xrange(len(Avals)):
        #print idx, Avals[idx]
        if Avals[idx] > Bvals[idx]:
            winner= 1
            break
        elif Avals[idx] < Bvals[idx]:
            winner= -1
            break
    
    print str(winner) + ' got the highest card'
    return winner
"""   
    
print isflush('TS TC TH TD AS') 
print isflush('TS TC TH 2D AS') 
print isflush('8C TC KC 9C 4C') 

print is_straight('2S 3C 4H 5D 6S') 
print is_straight('TS JC QH KD AS') 
print is_straight('4C TC KC 9C 4C') 

print getHighestCard('2S 3C 4H 5D 6S',1) 
print getHighestCard('TS JC QH KD AS',2) 
print getHighestCard('4C TC KC 9C 4C',3) 

print is_straight_flush('TS TC TH TD AS') 
print is_straight_flush('2S 3C 4H 5D 6S') 
print is_straight_flush('2S 3S 4S 5S 6S') 

print is_royal_flush_winner('AS KS QS JS TS') 
print is_royal_flush_winner('7S 3C 4H 5D 6S') 
print is_royal_flush_winner('2S 3S 4S 5S 6S') 


print is_n_of_a_kind('TS TC TH TD AS',5) 
print is_n_of_a_kind('TS TC TH 2D AS',3) 
print is_n_of_a_kind('8C TC KC 9C 4C',2) 


print is_two_pairs('TS TC 8H 8D AS') 
print is_two_pairs('TS TC 7H 7D 7S') 
print is_two_pairs('8C 8C KC 9C 4C') 


print is_full_house('TS TC 8H 8D AS') 
print is_full_house('TS TC 7H 7D 7S') 
print is_full_house('8C 8C KC 9C 4C') 


print flush_winner('2S 3S 5S 6S 8S','2S 3S 5S 6S JS')
print flush_winner('2S 3S 5S 6S 8S','2S 3S 5S 6S JC')
print flush_winner('2S 3S 5S 6S 8C','2S 3S 5S 6S JS')

print straight_winner('2S 3S 5S 6S 7S','TS 3S 5S 6S 4C')
print straight_winner('2S 3S 5S 6S 7S','7S 3S 5S 6S 4C')
print straight_winner('2S 3S 5S KS 7S','7S 3S 5S 6S 4C')


print royal_flush_winner('AS KS QS JS TS','TS 3S 5S 6S 4C')
print royal_flush_winner('2S 3S 5S 6S 7S','TS KS QS JS AS')
print royal_flush_winner('AS KS QS JS TS','AS KS QS JS TS')


print straight_flush_winner('9S KS QS JS TS','AS KS QS JS TS')
print straight_flush_winner('2S 3S 5S 6S 7S','TS KS QS JS AS')
print straight_flush_winner('2S KS QS JS TS','2S KS QS JS TS')


print n_of_a_kind_winner('TS TC TH TD 2S','TS TC TH TD AS',4)
print n_of_a_kind_winner('TS TC TH 9D 4S','TS TC TH 9D 3S',3)
print n_of_a_kind_winner('TS TC TH TD AS','TS TC TH TD AS',4)

print full_house_winner('TS TC TH 8D 8S','8S 8C 8H TD TS') 
print full_house_winner('8S 8C 8H TD TS','TS TC TH 8D 8S') 
#print full_house_winner('TS TC 8H 8D 8S','8S 8C 8H JD JS') 
#print full_house_winner('TS TC 8H 8D 8S','JS JC JH 2D 2S') 



print two_of_a_pair_winner('TS TC 7H 8D 8S','8S 8C 6H TD TS') 
print two_of_a_pair_winner('8S 8C 3H TD TS','TS TC 2H 9D 9S') 
print two_of_a_pair_winner('JS JC AH 8D 8S','KS KC 8H 2D 2S') 
print two_of_a_pair_winner('TS TC 4H 8D 8S','9S 9C JH 4D 4S') """

totalwinner=0
counter = 0
for game in games:
    
    if game.strip()!='':
        A=game[0:15]
        B=game[15:]
        winner = 0
        counter+=1
        print counter, '********'
        if not winner: winner = royal_flush_winner(A,B)
        if not winner: winner = straight_flush_winner(A,B)
        if not winner: winner = n_of_a_kind_winner(A,B,4)
        if not winner: winner = full_house_winner(A,B)
        if not winner: winner = flush_winner(A,B)
        if not winner: winner = straight_winner(A,B)
        if not winner: winner = n_of_a_kind_winner(A,B,3)
        if not winner: winner = two_of_a_pair_winner(A,B)
        if not winner: winner = n_of_a_kind_winner(A,B,2)
        if not winner: winner = highest_card_winner(A,B)
        print A, B, winner
        totalwinner+=winner

print  'A won '+ str((counter+ totalwinner)/2) + ' games', 'B won '+ str((counter-totalwinner)/2)
    



    
    


    


# In[ ]:




# In[ ]:



