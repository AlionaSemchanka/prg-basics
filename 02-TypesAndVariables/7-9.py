import random
D_R= random.randint(1,6)
Special_number= D_R==1 or D_R==6
print(f'Dice rolled: {D_R}')
print(f'Special number(1 or 6): {Special_number}')