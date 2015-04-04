file = open('file.txt', 'r')

for line in file:
    print(line, end="")

print()

file = open('file.txt', 'r')

for line in file:
    print(line[0])

print()

file = open('file.txt', 'r')

for line in file:
    print(line[0], line[-2], sep="")

print()

file = open('file.txt', 'r')

for line in file:
    c = line[0] + line[-2]
    print(c * int(line[-2]))
