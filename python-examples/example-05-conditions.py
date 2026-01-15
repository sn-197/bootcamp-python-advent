# This example contains conditional statements in Python.

age = 20

if age > 18:   
    print("You are an adult.")
else:
    print("You are a minor.")


# Checking multiple conditions

construction_year = 2001
vehicle_type = "car"

if construction_year < 2000 and vehicle_type == "car":
    print("This car needs to be checked every 12 months.")
if construction_year >= 2000 or vehicle_type == "truck":    
    print("This vehicle needs to be checked every year.")

