#######################################
#
# addition.py
#
# A program to add two numbers. 
#######################################

# Get input from user.
num1 = input("Put a number in there! ")
num2 = input("Put another number in there! ")

# Convert the strings num1 and num2 to integers.
num1 = int(num1)   #If I want to input decimal, I need to change 'int' to 'float'
num2 = int(num2)

# Process data. Perform the addition.
result = num1 + num2

# Print/output results.
print("Result:", result)