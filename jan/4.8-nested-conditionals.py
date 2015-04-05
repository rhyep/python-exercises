# 4.8-nested-conditionals.py


value = eval(input('Please enter an integer value in the range 0...10: '))

if value >= 0:  # First check
    if value <= 10:  # Second check
        print('In range')
print('Done')


value = eval(input('Please enter an integer value in the range 0...10: '))

if value >= 0 and value <= 10:  # Only one, slightly more complicated check
    print('In range')
print('Done')


value = eval(input('Please enter an integer value in the range 0...10: '))

if value >= 0:  # First check
    if value <= 10:
        # Second check
        print(value, 'is in range')
    else:
        print(value, 'is too large')
else:
    print(value, 'is too small')
print('Done')


# Get number from the user
value = eval(input('Please enter an integer value in the range 0...1023: '))

# Create an empty binary string to build upon
binary_string = ''
# Integer must be less than 1024
if 0 <= value < 1024:
    if value >= 512:
        binary_string += '1'
        value %= 512
    else:
        binary_string += '0'
    if value >= 256:
        binary_string += '1'
        value %= 256
    else:
        binary_string += '0'
    if value >= 128:
        binary_string += '1'
        value %= 128
    else:
        binary_string += '0'
    if value >= 64:
        binary_string += '1'
        value %= 64
    else:
        binary_string += '0'
    if value >= 32:
        binary_string += '1'
        value %= 32
    else:
        binary_string += '0'
    if value >= 16:
        binary_string += '1'
        value %= 16
    else:
        binary_string += '0'
    if value >= 8:
        binary_string += '1'
        value %= 8
    else:
        binary_string += '0'
    if value >= 4:
        binary_string += '1'
        value %= 4
    else:
        binary_string += '0'
    if value >= 2:
        binary_string += '1'
        value %= 2
    else:
        binary_string += '0'
        binary_string += str(value)

#  Display the results
if binary_string != '':
    print(binary_string)
else:
    print('Cannot convert')


# Get number from the user
value = eval(input('Please enter an integer value in the range 0...1023: '))

# Initial binary string is empty
binary_string = ''

# Integer must be less than 1024
if 0 <= value < 1024:
    binary_string += str(value//512)
    value %= 512
    binary_string += str(value//256)
    value %= 256
    binary_string += str(value//128)
    value %= 128
    binary_string += str(value//64)
    value %= 64
    binary_string += str(value//32)
    value %= 32
    binary_string += str(value//16)
    value %= 16
    binary_string += str(value//8)
    value %= 8
    binary_string += str(value//4)
    value %= 4
    binary_string += str(value//2)
    value %= 2
    binary_string += str(value)

# Report results
if binary_string != '':
    print(binary_string)
else:
    print('Unable to convert')


# troubleshoot
print('Help! My computer doesn't work!')
print('Does the computer make any sounds (fans, etc.)')
choice = input('or show any lights? (y/n):')
# The troubleshooting control logic
if choice == 'n':  # The computer does not have power
    choice = input('Is it plugged in? (y/n):')
    if choice == 'n':  # It is not plugged in, plug it in
        print('Plug it in. If the problem persists, ')
        print('please run this program again.')
    else:  # It is plugged in
        choice = input('Is the switch in the \'on\' position? (y/n):')
        if choice == 'n':  # The switch is off, turn it on!
            print('Turn it on. If the problem persists, ')
            print('please run this program again.')
        else:  # The switch is on
            choice = input('Does the computer have a fuse? (y/n):')
            if choice == 'n':  # No fuse
                choice = input('Is the outlet OK? (y/n):')
                if choice == 'n':  # Fix outlet
                    print('Check the outlet's circuit ')
                    print('breaker or fuse. Move to a')
                    print('new outlet, if necessary. ')
                    print('If the problem persists, ')
                    print('please run this program again.')
                else:  # Beats me!
                    print('Please consult a service technician.')
            else:  # Check fuse
                print('Check the fuse. Replace if ')
                print('necessary. If the problem ')
                print('persists, then ')
                print('please run this program again.')
else:  # The computer has power
    print('Please consult a service technician.')


# File timeconvcond1.py

# Some useful conversion factors
seconds_per_minute = 60
seconds_per_hour = 60 * seconds_per_minute  # 3600

# Get user input in seconds
seconds = eval(input('Please enter the number of seconds:'))

# First, compute the number of hours in the given number of seconds
hours = seconds // seconds_per_hour  # 3600 seconds = 1 hour
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % seconds_per_hour
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // seconds_per_minute  # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % seconds_per_minute
# Report the results
print(hours, end='')
# Decide between singular and plural form of hours
if hours == 1:
    print(' hour ', end='')
else:
    print(' hours ', end='')
print(minutes, end='')
# Decide between singular and plural form of minutes
if minutes == 1:
    print(' minute ', end='')
else:
    print(' minutes ', end='')
print(seconds, end='')
# Decide between singular and plural form of seconds
if seconds == 1:
    print(' second')
else:
    print(' seconds')


# File timeconvcond2.py
# Some useful conversion constants
seconds_per_minute = 60
seconds_per_hour = 60 * seconds_per_minute  # 3600
seconds = eval(input('Please enter the number of seconds:'))
# First, compute the number of hours in the given number of seconds
hours = seconds // seconds_per_hour  # 3600 seconds = 1 hour
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % seconds_per_hour
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // seconds_per_minute  # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % seconds_per_minute
# Report the results
if hours > 0:  # Print hours at all?
    print(hours, end='')
    # Decide between singular and plural form of hours
    if hours == 1:
        print(' hour ', end='')
    else:
        print(' hours ', end='')
if minutes > 0:  # Print minutes at all?
    print(minutes, end='')
    # Decide between singular and plural form of minutes
    if minutes == 1:
        print(' minute ', end='')
    else:
        print(' minutes ', end='')
    # Print seconds at all?
if seconds > 0 or (hours == 0 and minutes == 0 and seconds == 0):
    print(seconds, end='')
    # Decide between singular and plural form of seconds
    if seconds == 1:
        print(' second', end='')
    else:
        print(' seconds', end='')
print()  # Finally print the newline


# digit to word
value = eval(input('Please enter an integer in the range 0...5: '))
if value < 0:
    print('Too small')
else:
    if value == 0:
        print('zero')
    else:
        if value == 1:
            print('one')
        else:
            if value == 2:
                print('two')
            else:
                if value == 3:
                    print('three')
                else:
                    if value == 4:
                        print('four')
                    else:
                        if value == 5:
                            print('five')
                        else:
                            print('Too large')
print('Done')
