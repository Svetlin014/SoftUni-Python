print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_value = total_bill * tip_percentage / 100
tip_per_peron = (total_bill + tip_value) / total_people
print(f"Each person should pay: {tip_per_peron:.2f}$")
