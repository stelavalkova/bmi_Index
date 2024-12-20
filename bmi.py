print("Welcome to the BMI calculator!")
weight = int(input("What is your weight? "))
print("Great!")
height = float(input("What is your height in decimal,please? "))
print("Your result:")
# height_index = float(input("What is your height in decimal,please? ") * 2)
BMI = int(weight / (height ** 2))
print("Your BMI is: " + str(BMI))

if BMI >= 25:
    print("You are overweight!")
elif BMI >= 18:
        print("Your weight is normal!")
else:
    print("You are underweight!")