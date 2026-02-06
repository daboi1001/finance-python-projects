fhand = open('stock_profit_checker.py')
temp = fhand.read()
lines = temp.splitlines()
count = 0
for line in temp:
    count = count + 1
print('Line COunt:', len(lines))

print(len(temp))

print(temp[:90 ])