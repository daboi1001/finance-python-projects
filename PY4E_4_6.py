def computepay(h, r):
    if hrs > 40:
        overtimehrs = hrs - 40
        overtimerate = rate * 1.5
        pay = (hrs - overtimehrs) * rate + overtimehrs * overtimerate
        return pay
    else:
        pay = rate * hrs
        return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pay = computepay(hrs, rate)
print("Pay", pay)