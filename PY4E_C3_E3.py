score = input("Enter Score between 0.0 & 1.0: ")

try:
    score = float(score)
except:
    print('Your input was not within the desired range. Please try again.')
    quit()

#print(type(score))
#print(score)

if score<=1.0 and score>=0.0:
    if score>=.9:
        grade = 'A'
    elif score>=.8:
        grade = 'B'
    elif score >=.7:
        grade = 'C'
    elif score>=.6:
        score = 'D'
    else:
        score = 'F'
    print(grade)
else:
    print('Your input was not within the desired range. Please try again.')