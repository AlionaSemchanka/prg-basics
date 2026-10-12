price= input('price: ')
p= float(price)
discount= input('discount: ')
d=int(discount)
price_w_d= p-p*d/100
price_w= round(price_w_d,2)
Red=p-price_w_d
R=round(Red, 2)
print('Enter price: ', p)
print('Enter discount: ', d)
print('Price wiht discount: ', price_w)
print('Reduction: ', R)