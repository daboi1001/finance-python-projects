hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hrs > 40:
    overtimehrs = hrs - 40
    overtimerate = rate * 1.5
    pay = (hrs - overtimehrs) * rate + overtimehrs * overtimerate
else:
    pay = rate * hrs
    
print(pay)
print(overtimehrs)
print(overtimerate)
print(hrs)
print(rate)