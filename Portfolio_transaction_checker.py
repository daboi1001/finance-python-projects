buycount = 0
sellcount = 0
totalinv = 0
totalback = 0
fn = input('Enter Desired File Name: ')
fhand = open(fn)
for line in fhand:
    line = line.strip()
    parts = line.split()
    action = parts[0]
    ticker = parts [1]
    shares = parts[2]
    price = parts[3]
    
    if line.startswith('BUY'):
        buycount = buycount + 1
        
        totalinv = totalinv + (float(price) * int(shares))
    elif line.startswith('SELL'):
        sellcount = sellcount + 1
        totalback = totalback + (float(price)* int(shares))
print('Your total invested was:', totalinv)
print('Your total recieved was:', totalback)
print('Number of Buy Trades', buycount)
print('Number of Sell Trades', sellcount)
if totalback > totalinv:
    print('Congrats! You made a profit of:', totalback-totalinv)
elif totalback == totalinv:
    print('You broke even.')
else:
    print('Better luck next time. You lost:', abs(totalback-totalinv))