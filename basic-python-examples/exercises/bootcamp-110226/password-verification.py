# this is a password verification program that checks if the password given by the user is correct


# set the correct password
correct_password = "password123"    

# get user input
password = input("Enter the password: ")

# check if the password is correct
if password == correct_password:
    print("Access granted.")    
else:    print("Access denied. Incorrect password. Try again.")

# check how many times the user has given a password entry
attempts = 1
while password != correct_password and attempts < 3:
    password = input("Enter the password: ")
    attempts += 1
if password == correct_password:
    print("Access granted.") 
else:    print("Access denied. Too many attempts.")


# todos: 
# fix double access granted message if the password is correct on the first try
# show message after second message is incorrect