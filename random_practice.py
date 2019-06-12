import random
name = input("Enter your name:")

salary = int(input("Enter your salary:"))
print(f"{name} your current salary is {salary}")
raise_per = (random.randint(1,100))
print(f"your raise is {str(raise_per)}% of {salary}")
raise_amount = salary*(raise_per/100)+ salary
print(f"{name},your new salary is {raise_amount}")