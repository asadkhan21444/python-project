# INPUT WE NEED  FROM THE  USER 
# total rent
# total order food for snacking
# Electricity units spends
# charge per unit 
# person living room/flat

# ...........................

# output
#  total amount you have to pay

# Hostel/Flat rent input
rent = int(input("Enter your hostel/flat rent: "))

# Food input
food = int(input("Enter the amount of food orders: "))

# Electricity input
Electricity_spend = int(input("Enter the electricity units spent: "))

# Per unit charge
charge_per_unit = int(input("Enter the charge per unit: "))

# Number of persons
persons = int(input("Enter the number of persons living in the flat: "))

# Total electricity bill
total_bill = Electricity_spend * charge_per_unit

# Total amount divided per person
total_amount = (rent + food + total_bill) // persons

# Output
print("Each person will pay:", total_amount)
