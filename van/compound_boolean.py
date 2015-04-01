# compound boolean
a = 1
b = 2

if not a == b and not b == 0:
    print("a = b, b = 0")
else:
    print("nothing")
if a == 1 and b == 2:
    print("and!")
if a == b or b == 0:
    print("or!")
