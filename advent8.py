file = open("av8.txt","r")

lines = file.readlines()

Ldict= {}
Rdict = {}

input = lines[0]

print(input)

p2 = []

for j in range(2, len(lines)):
    if lines[j][2] == 'A':
        p2.append(lines[j][0:3])      

for i in range(2,len(lines)):
    Ldict[lines[i][0:3]]= lines[i][7:10]
    Rdict[lines[i][0:3]]= lines[i][12:15]

step = 0
steps=0
p2end=0

while p2end != 6:
    step+=1
    p2end=0
    for i in range(0, len(p2)):
        if input[step] =="L":
            left=Ldict[p2[i]]
            p2[i] = left
        elif input[step] == "R":
            right = Rdict[p2[i]]
            p2[i] = right
        if p2[i][2] == "Z":
            p2end+=1
        if step%269 == 0:
            steps+=269
            step=0
    if p2end >=3:
        print(p2)
tot = step+steps
print(step)
print(steps)
print(tot)

step = 0
steps = 0
head = "AAA"      

while head != "ZZZ":
    if input[step] == "L":
        step +=1
        left = Ldict[head]
        head = left
    elif input[step] == "R":
        step+=1
        right = Rdict[head]
        head = right 
    if step%269 ==0:
       steps+=269    
       step=0

tot = steps + step

print(step)
print(steps)
print(tot)
    

