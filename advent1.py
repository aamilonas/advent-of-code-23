file = open("av1.txt","r")

lines = file.readlines()

allnums = []

for line in lines:
   l, r = 0, len(line)-1
   val1, val2 = 69, 69

   while l!=r:
        if line[l].isdigit():
           val1 = line[l]
        if line[r].isdigit():
            val2=line[r]
        l+=1
        r-=1
        if val1!=69 and val2!=69:
            break
        
   if val1!= 69 and val2!=69:
        oval = str(val1)+str(val2)
        allnums.append(int(oval))

print(allnums)


file.close()
