age_human=int(input('Enter the dogs age in human years: '))
age_dog=0
if age_human>=0 and age_human<=2:
    age_dog=age_human*10.5
elif age_human>2:
    age_dog=2*10.5+(age_human-2)*4
print(f'The dogs age in dogs years is {age_dog} years.') 
