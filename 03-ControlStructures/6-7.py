age= int(input('Enter your age: '))
if age<13:
    group='Child'
elif age>=13 and age<=19:
    group= 'Teen'
elif age>=20 and age<=64:
    group='Adult'
elif age>65:
    group='Senior'
else:
    print('You do not belong to any of the age groups.')
print(f'You belong to {group}')