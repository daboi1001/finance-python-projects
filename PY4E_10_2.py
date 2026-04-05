times = []
d = {}
fname = input("Enter File Name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand:
    if line.startswith("From "):
        temp = tuple(line.split())
        for word in temp:
            if ":" in word:
                times.append(word[:2])
#print(times)

for time in times:
    d[time] = d.get(time,0)+1

finalTimes = list(sorted(d.items()))
#print(finalTimes)

for hour,count in finalTimes:
    print(hour,count)
