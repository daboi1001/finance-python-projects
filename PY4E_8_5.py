emailList =[]
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if line.startswith("From "):
        line = line.rstrip()
        temp = list(line.split())
        #print(temp)
        emailList.append(temp[1])

#print(emailList)
count = len(emailList)
for email in emailList:
    print(email)
print("There were", count, "lines in the file with From as the first word")
