###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
temperature=float(input('Enter temperature in degrees Celsius: '))
# Convert temperature to Fahrenheit
temperature_kelvin=temperature+273.15
# Print the result 
print(f'Temperature in degrees Kelvin: {round(temperature_kelvin, 2)}')