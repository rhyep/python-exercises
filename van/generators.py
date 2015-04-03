# generators
count = 0


def remember():
    global count  # global is a reserved word
    count += 1
    print(count)

remember()
remember()
remember()
remember()
remember()

# yield - another kind of generatord


def gen():
    yield 3
    yield "wow"
    yield 1.3
    yield -4
x = gen()
print(x)
print(type(x))
print(gen())
print(next(x))
