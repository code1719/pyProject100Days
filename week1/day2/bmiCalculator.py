height = input("What is your height?")

weight = input("What is your weight?")

new_height = float(height)

new_weight = int(weight)

bmi = new_weight / new_height ** 2

print("Your BMI is " + str(bmi))