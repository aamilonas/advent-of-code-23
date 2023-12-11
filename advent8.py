file = open("av8.txt","r")

lines = file.readlines()

Ldict= {}
Rdict = {}

input = lines[0]

print(input)

l1 = lines[2][0:3]

l2 =lines[2][7:10]
l3 = lines [2][12:15]

print(l1)
print(l2)
print(l3)

for i in range(2,len(lines)):
    Ldict[lines[i][0:3]]= lines[i][7:10]
    Rdict[lines[i][0:3]]= lines[i][12:15]

step = 0
steps = 0
head = "AAA"

test1 = "JST"
teststep = 1
for c in input:
    if c == "L":
        teststep +=1
        left = Ldict[test1]
        test1 = left
    elif c == "R":
        teststep+=1
        right = Rdict[test1]
        test1 = right
print("test ended at:" + str(teststep) + ", " + test1)

        

while head != "ZZZ":
    if step == 0:
        print(head +":"+ Ldict[head] +""+ Rdict[head])
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
       print(input[step-5:step])
       step=0

tot = steps + step

print(step)
print(steps)
print(tot)
    

