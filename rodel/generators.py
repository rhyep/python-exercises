# generators.py

count = 0


def remember():
    global count  # set count as global variable
    count += 1
    print(count)

remember()
remember()
remember()
remember()
remember()
remember()


# yield

def gens():
    yield 3
    yield "wow"
    yield 1.3
    yield -4

print(gens)
print(type(gens))
print(gens())
x = gens()
y = gens()
print(type(x))
print(x)
print(x, y)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
