# Electricity Bill Calculator  

name = input("enter customer name: ")

previous = float(input("Enter previous meter reading: "))

current = float(input("Enter current meter reading: "))

RATE = 12.90
 
if name == "" :
 print("name must not be blank ")
 name = input("enter customer name: ")

elif previous <= 0:
 print("previous meter reading must be atleast 0")
 previous = float(input("Enter previous meter reading: "))

elif current < previous:
 print("current reading must be atleast the previous reading")
 current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("Customer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
