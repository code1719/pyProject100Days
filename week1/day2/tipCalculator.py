#if the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip; Ther eare 2 ways to round a number. You might have to do some googling

#code follows;

print("Welcome to the tip calculator! ")
total_bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? ")
bill_split = input("How many people are splitting the bill? ")

new_total = float(total_bill)
new_tip = float(tip) * 0.01
new_bill_split = int(bill_split)


#print(type(new_total))
#print(type(new_tip))
#print(type(new_bill_split))

each_pay = new_total / new_bill_split * (1 + new_tip)
new_each_pay = str(round(each_pay, 2))

print(f"Each person should pay {new_each_pay}")