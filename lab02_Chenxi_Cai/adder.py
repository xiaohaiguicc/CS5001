# Takes input from the user in the form of numerical values,
# and prints out a sentence reporting the sum of the values
def main():
    num1 = input('Enter a first value: ')
    num2 = input('Enter a second value: ')
    num_sum = int(num1) + int(num2)
    
    print('The sum of', num1, '+', num2, 'is', num_sum)

main()