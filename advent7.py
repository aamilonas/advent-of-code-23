file = open("av3.txt","r")

lines = file.readlines()

cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
hands = []
bids = [] 
rank=[]

for i, line in enumerate(lines):
    x = line.split(' ')
    hands[i] =x[0]
    bids[i] = x[1]
    
