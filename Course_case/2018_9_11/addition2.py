#######################################
#
# addition2.py
#
# A program to add two numbers. The
# difference between this program and
# addition.py is that we convert the
# input string to an integer in one
# step.
#######################################

# Get input from user.
num1 = int(input("Put a number in there! "))
num2 = int(input("Put another number in there! "))  

'''
If I remove the 'int', then the output of plus is string1string2, shown below.
'''

# num1 = input("Put a number in there! ")
# num2 = input("Put another number in there! ")


# Process data by adding the two numbers.
result = num1 + num2

# Print/output results.
print("Result:", result)