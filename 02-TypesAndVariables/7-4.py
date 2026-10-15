circumference=int(input('Enter tree circumference in cm: '))
diameter=circumference/3.14159
diameter_t=diameter>=50
print(f'Tree can be cut down: {diameter_t}')