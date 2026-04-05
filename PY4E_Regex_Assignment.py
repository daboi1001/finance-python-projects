import re
sumList =[]
fhand = open('regex_sum_2345901.txt')
for line in fhand:
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        int_list=[int(value) for value in x]
        xSum = sum(int_list)
        sumList.append(xSum)

print('Your total sum is ' + str(sum(sumList)) +'.')
