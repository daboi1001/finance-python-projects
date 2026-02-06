buyprice = float(input('What did you buy the stock at?     '))
sellprice = float(input('What did you sell the stock at?    '))
stockcount = float(input('How many stocks did you purchase?  '))

amtinvested = buyprice * stockcount
amtback = sellprice * stockcount

print('Your total cost is $'+ str(amtinvested))
print('Your total revenue is $'+ str(amtback))



if amtback < amtinvested:
    print('Your trade resulted in a loss of $'+ str(amtinvested-amtback))
elif amtback == amtinvested:
    print('You broke even')
else:
    print('Your trade resulted in a profit of $'+ str(amtback-amtinvested) + '. Congratulations!')