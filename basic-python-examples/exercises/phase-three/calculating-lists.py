# This file does basic calculations on lists.
# It uses the built-in sum() and len() functions to calculate the sum and average of a list of numbers.
# Other funtion included is max() to find the maximum value(s) in the list.


# step 1: define a list of random numbers
numbers = [12345, 99999, 0, -12345, -99999]

# step 2: calculate the sum of the numbers
total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")

# step 3: calculate the average of the numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(f"The average of the numbers is: {calculate_average(numbers)}")

# step 4: find the maximum value in the list
max_value = max(numbers)
print(f"The maximum value in the list is: {max_value}")

