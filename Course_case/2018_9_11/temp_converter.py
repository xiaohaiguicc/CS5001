#######################################
#
# temp_converter.py
#
#######################################

# By convention, constants are named with all 
# caps. There is no support in Python for ensuring
# that constants remain unchanged. 
BASE = 32
CONVERSION_FACTOR = 5.0/9.0

# Get input from user.
fahrenheitTemp = input("Input a temperature in Farhenheit: ")

celsiusTemp = (float(fahrenheitTemp) - BASE) * CONVERSION_FACTOR

# Print/output results.
print("That would be", round(celsiusTemp, 2), "degrees Celsius")