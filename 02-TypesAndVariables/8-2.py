# Calculation of circle area and circumference 
r=float(input('Enter radius: '))
PI=3.14
# determine radius and PI values
circumference=2*PI*r
# calculate circumference 
print(f'The circumference of the circle is: {round(circumference, 2)}')
# print results
area=PI*r**2
# calculate area
print(f'The area of the circle is: {round(area, 2)}')
# print results