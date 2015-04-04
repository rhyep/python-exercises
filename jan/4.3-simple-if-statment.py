# 4.3-simple-if-statment.py


# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    print(dividend, '/', divisor, '=', dividend/divisor)


# general form of if
'''
if condition:
    block
'''
# if
# condition
# colon
# block


# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    quotient = dividend/divisor
print(dividend, '/', divisor, '=', quotient)
print('Program finished')


# Request input from the user
num = eval(input('Please enter an integer in the range 0...9999: '))
# Attenuate the number if necessary

if num < 0:
    num = 0  # Make sure number is not too small
if num > 9999:
    num = 9999  # Make sure number is not too big
print(end="[")  # Print left brace

# Extract and print thousands-place digit
digit = num//1000  # Determine the thousands-place digit
print(digit, end='')  # Print the thousands-place digit
num %= 1000  # Discard thousands-place digit

# Extract and print hundreds-place digit
digit = num//100  # Determine the hundreds-place digit
print(digit, end='')  # Print the hundreds-place digit
num %= 100  # Discard hundreds-place digit

# Extract and print tens-place digit
digit = num//10  # Determine the tens-place digit
print(digit, end='')  # Print the tens-place digit
num %= 10  # Discard tens-place digit

# Remainder is the one-place digit
print(num, end='')  # Print the ones-place digit

print("]")  # Print right brace
