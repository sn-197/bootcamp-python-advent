# This exercise demonstrates the difference between mutable and immutable values in Python.


# Intro: (im)mutable values 
immutable_int = 10
immutable_str = "Hello, World!"
mutable_list = [1, 2, 3]
mutable_set = {1, 2, 3}


# Exercise 1: Print y after changing x
x = 55
y = x
x = 75
print(y)

# spoiler alert:
# 
# y = 55 because integers are immutable, and changing x does not affect y.
#
# Python execution steps:
#
# 1. x is assigned the value 55.      
# 2. y is assigned the value of x (which is 55).
# 3. x is reassigned to 75, but y remains 55.



# Exercise 2: Print b after adding 1 to a
a = 3
a = a + 1
b = a
print(b)

# spoiler alert:
#
# b = 4 because integers are immutable, and b gets the value of a after a is updated.


# Exercise 3: Working with immutable strings
s1 = "Hello"
s2 = s1 + ", World!"
print(s1)
print(s2)

# spoiler alert:
#
# s1 = "Hello" and s2 = "Hello, World!" because strings are immutable, and concatenation creates a new string.


# LEARINING BITE
#
# A small conceptual thing worth mentioning:
# Python variables don’t “contain values” — they reference objects.
#
# Right now, the exercises imply that immutability means “changing one variable doesn’t affect another.” 
# That’s true, but looking at exercise 1, the deeper reason is:
# 
# x = 55 x points to an integer object 55
#
# y = x → y points to the same object
#
# x = 75 → x now points to a different object
#
# Nothing was “changed” — the reference changed.
# 
# And why this matters, you may wonder? 
# This has to do with mutable examples, where references do matter.


# Exercise 4: Print after modifying a value in a list
list1 = [1, 2, 3]
list1[0] = 10
print(list1)

# spoiler alert:
# list1 = [10, 2, 3] because lists are mutable, and modifying an element changes the list in place.


# Exercise 5: Adding a value to a list
list2 = [4, 5, 6]
list2.append(7)
print(list2)

# spoiler alert:
# list2 = [4, 5, 6, 7] because lists are mutable, and appending adds an element to the existing list.


# Exercise 6: Removing a value from a list
list3 = [8, 9, 10]
list3.remove(9)
print(list3)

# spoiler alert:
# list3 = [8, 10] because lists are mutable, and removing an element modifies the list in place.


# Exercise 7: Print after modifying
nums = [10, 20]
copy_nums = nums
nums.append(30) 
print(nums)
print(copy_nums)

# spoiler alert:
# Both nums and copy_nums will print [10, 20, 30] because lists are mutable.
# The variables reference the same list object.