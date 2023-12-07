file = open("av3.txt","r")

lines = file.readlines()
symboldict = {'!','@','#','$','%','^','*','(',')','-','+', '='}

arr = [[c for c in line] for line in lines]

for i,line in enumerate(lines):
    print(i)
    print(line)
    for j,c in enumerate(line):
        if c in symboldict:
            arr[i][j] = c
        if c.isdigit():
            arr[i][j] = c

for row in arr:
    print(row)


