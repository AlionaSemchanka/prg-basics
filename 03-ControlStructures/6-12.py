number_of_products=int(input('Number of products purchased: '))
price=float(input('Product price: '))
if number_of_products>2:
    amount = 2 * price + (number_of_products - 2) * price * 0.75
else:
    amount=number_of_products*price
print(f'Amount to pay: {amount:.2f} ')
