largest = None
smallest = None
#numlist=[]
while True:
    num = input("Enter a number: ")
    try: 
       if num == 'done':
          break
       else:
          num = int(num)
    except:
       print('Invalid input')
       continue
    
    if smallest is None:
        smallest = num
    else:
        if smallest > num:
            smallest = num
    if largest is None:
        largest = num
        #print(num)
        #continue
    else:
           if largest < num:
            largest = num 

print("Maximum is", largest)
print("Minimum is", smallest)