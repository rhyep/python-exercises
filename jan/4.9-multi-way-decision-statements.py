# 4.9-multi-way-decision-statements.py

# other digit to word
value = eval(input('Please enter an integer in the range 0...5: '))
if value < 0:
    print('Too small')
elif value == 0:
    print('zero')
elif value == 1:
    print('one')
elif value == 2:
    print('two')
elif value == 3:
    print('three')
elif value == 4:
    print('four')
elif value == 5:
    print('five')
else:
    print('Too large')
print('Done')


# datetransformer.py
month = eval(input('Please enter the month as a number (1-12): '))
day = eval(input('Please enter the day of the month: '))
# Translate month into English
if month == 1:
    print('January ', end='')
elif month == 2:
    print('February ', end='')
elif month == 3:
    print('March ', end='')
elif month == 4:
    print('April ', end='')
elif month == 5:
    print('May ', end='')
elif month == 6:
    print('June ', end='')
elif month == 7:
    print('July ', end='')
elif month == 8:
    print('August ', end='')
elif month == 9:
    print('September ', end='')
elif month == 10:
    print('October ', end='')
elif month == 11:
    print('November ', end='')
else:
    print('December ', end='')
# Add the day
print(day, 'or', day, end='')
# Translate month into Spanish
if month == 1:
    print(" de enero")
elif month == 2:
    print(" de febrero")
elif month == 3:
    print(" de marzo")
elif month == 4:
    print(" de abril")
elif month == 5:
    print(" de mayo")
elif month == 6:
    print(" de junio")
elif month == 7:
    print(" de julio")
elif month == 8:
    print(" de agosto")
elif month == 9:
    print(" de septiembre")
elif month == 10:
    print(" de octubre")
elif month == 11:
    print(" de noviembre")
else:
    print(" de diciembre")
