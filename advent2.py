file = open("av2.txt","r")

lines = file.readlines()

colors = ['Game', 'red', 'blue', 'green']

p1dict = {"red": 12 , "green": 13, "blue": 14}

toremove = {ord(','): '', ord('\n'): ''}

#sums totals of games: print(x[0][5:])
p1_gametot = 0
p2_gametot =0


for line in lines:
    x = line.split(':')
    rounds = x[1].split(';')
    addToTot = True
    p2dict = {"red": 0 , "green": 0, "blue": 0}
    power=1

    for round in rounds:
        cubes = round.split(' ')
        for d,val in enumerate(cubes):
            if (cubes[d].translate(toremove)) in p1dict.keys():
                if int(cubes[d-1]) > p1dict[cubes[d].translate(toremove)]:
                    addToTot = False
                if int(cubes[d-1])>p2dict[cubes[d].translate(toremove)]:                
                   p2dict[cubes[d].translate(toremove)] = int(cubes[d-1]) 
    if addToTot:
            p1_gametot += int(x[0][5:])
    for n in list(p2dict.values()):
        power = power*n
    p2_gametot += power
print(p1_gametot)
print(p2_gametot)
        



                    

    
