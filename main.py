print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people_split = int(input("How many people to split the bill?\n"))
each_pay = round(int(((total_bill/people_split)*(1+tip))), 2)
print(f"Each person should pay {each_pay} dollar.")
