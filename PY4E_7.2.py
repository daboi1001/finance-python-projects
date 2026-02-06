total = 0
count = 0
fname=input('Enter Desired File Name: ')
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    lnvalue = float(line [19: ])
    total = total + lnvalue
    
final = str(total/count)
print("Average spam confidence: " + final)