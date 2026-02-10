# creat a program that asks the user for a number and determines if the number is odd or even


# get user input
number = int(input("Enter a number: "))

# determine if the number is odd or even
if number % 2 == 0:
    print(f"{number} is een even getal.")
else:    print(f"{number} is een oneven getal.")