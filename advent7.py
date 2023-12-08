file = open("av3.txt","r")

lines = file.readlines()

cards = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
hands = []
bids = [] 
ranks=[]
ctype = []

for i, line in enumerate(lines):
    x = line.split(' ')
    hands[i] =x[0]
    bids[i] = x[1]
    thisdict = {}
    #putting hand into dictionary
    for card in hands[i]:
        if card in thisdict:
            thisdict[card]+=1
        else:
            thisdict[card]=int(1)
    if 5 in thisdict.values():
        ctype[i] = 7
    elif 4 in thisdict.values():
        ctype[i] = 6
    elif sorted(thisdict.values())==[2,3]:
        ctype[i] = 5
    elif sorted(thisdict.values()) == [1,1,3]:
        ctype[i] = 4
    elif sorted(thisdict.values()) == [1,2,2]:
        ctype[i] = 3
    elif sorted(thisdict.values()) == [1,1,1,2]:
        ctype[i] = 2
    else:
        ctype[i] = 1
    
    ranks[i] = i

    indexing_length = len(ranks)-1
    sorted = False

    for n in range(0, indexing_length):

        



