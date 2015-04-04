# 4.6-pass-statement.py

x = 1

if x < 0:
    # Do nothing (This will not work!)
    print("fail")
else:
    print(x)

# pass
if x < 0:
    pass  # Do nothing
else:
    print(x)
