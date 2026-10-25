number = int(input("Enter decimal number: "))
n = number
binary = ""
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2
print(f"{number}(10) = {binary}(2)")