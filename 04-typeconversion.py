
name=input("What is your name? ")

# ask someone's birthday and calculate their age

birth_year = int(input("Year of Birth: ") )
# need to convert input from str into int
age = 2024 - birth_year
print(name+" is "+str(age))

# ask user their weight in pounds and convert into kilograms

weight_pounds = float(input("Enter your weight in pounds: "))
weight_kg = round((weight_pounds * 0.45359237),2)
print("You weigh "+str(weight_kg)+" kg")