emailList =[]
at = "@"
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if at in line:
        temp = list(line.split())
        for word in temp:
            if at in word:
                emailList.append(word)

#print(emailList)
for email in emailList:
    print(email)