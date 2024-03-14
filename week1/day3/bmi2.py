height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = weight / height ** 2

print("Your BMI is " + str(bmi))

if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 25:
    print("You have a normal BMI.")
elif bmi <= 30:
    print("You are slightly overweight.")
elif bmi <= 35:
    print("You are obese.")
else:
    print("You are severely obese.")
