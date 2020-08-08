products = {}

while True:
    command = input().split()
    if command == 'buy':
        break


    if product not in products:
        products[product] = quantity * price
    else:
        products[product] += quantity * price
    command = input().split()
print(products)