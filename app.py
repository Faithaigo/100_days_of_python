print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip woulldd you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill? "))

total_tip = total_bill * (tip / 100)

total = (total_bill + total_tip) / split

print(f"Each person should pay: ${round(total, 2)}")
