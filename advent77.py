import re
from collections import Counter

file = open("av7.txt","r")

lines = file.readlines()

cards = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':1,'Q':11,'K':12,'A':13}
hands = []
bids = [] 
ranks=[]
ctype = []

def strength(hand):
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('9')+2))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))
    C= Counter(hand)

    if part2:
        target = list(C.keys())[0]
        for k in C:
            if k!='1':
                if C[k]> C[target] or target =='1':
                    target = k
        assert target != '1' or list(C.keys())==['1']
        if'1' in C and target !='1':
            C[target] += C['1']
            del C['1']
        assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'



    if list(C.values()) == [5]:
        return (10,hand)
    elif sorted(C.values()) ==[1,4]:
        return (9,hand)
    elif sorted(C.values()) ==[2,3]:
        return (8,hand)
    elif sorted(C.values()) == [1,1,3]:
        return (7,hand)
    elif sorted(C.values()) == [1,2,2]:
        return (6,hand)
    elif sorted(C.values()) == [1,1,1,2]:
        return (5,hand)
    elif sorted(C.values()) == [1,1,1,1,1]:
        return (4, hand)
    else:
        assert False, f'{C} {hand} {sorted(C.values())}'

for line in lines:
    hand,bid = line.split()
    hands.append((hand,bid))
hands = sorted(hands, key=lambda hb:strength(hb[0]))
ans=0
for i, (h,b) in enumerate(hands):
    ans += (i+1)*int(b)

print(ans)
