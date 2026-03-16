fname = input("Enter file name: ")
fhand = open(fname)
romeoList = []

for line in fhand:
    #print(line.rstrip())
    #print(line.split())
    tempList = list(line.split())
    for word in tempList:
        if word not in romeoList:
            romeoList.append(word)

romeoList.sort()
print(romeoList)