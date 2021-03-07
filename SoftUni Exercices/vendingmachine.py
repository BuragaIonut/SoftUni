
s = 0
total_price = 0
while True:
    coin = input()
    if coin == 'Start':
        break
    else:
        coin = float(coin)
    if coin == 0.10 or coin == 0.20 or coin == 0.50 or coin == 1.00:
        s += coin
    else:
        print(f'Cannot accept {coin:.2f}')
while True:
    command = input()
    if command == 'Nuts':
        price = 2.0
        s = s - price
        if s >= 0:
            print(f'Purchased {command}')
        else:
            print('Sorry, not enough money')
            change = s + price
    elif command == 'Water':
        price = 0.7
        s = s - price
        if s >= 0:
            print(f'Purchased {command}')
        else:
            print('Sorry, not enough money')
            change = s + price
    elif command == 'Crisps':
        price = 1.5
        s = s - price
        if s >= 0:
            print(f'Purchased {command}')
        else:
            print('Sorry, not enough money')
            change = s + price
    elif command == 'Soda':
        price = 0.8
        s = s - price
        if s >= 0:
            print(f'Purchased {command}')
        else:
            print('Sorry, not enough money')
            change = s + price
    elif command == 'Coke':
        price = 1.0
        s = s - price
        if s >= 0:
            print(f'Purchased {command}')
        else:
            print('Sorry, not enough money')
            change = s + price
    elif command == 'End':
        change = s + price
        print(f'Change: {change:.2f}')
        break
    else:
        print('Invalid product')

