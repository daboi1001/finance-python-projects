emailList =[]
counts ={}
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
        
for email in emailList:
    counts[email] = counts.get(email,0)+1

#print(counts)

commonEmail = None
commonEmailCount = 0

for email, count in counts.items():
    if commonEmail is None or count > commonEmailCount:
        commonEmail = email
        commonEmailCount = count

print(commonEmail, commonEmailCount)