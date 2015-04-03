# file objects
f = open('file.txt', 'r')
# for L in f:
#   print(L[0])

# for L in f:
#   print(L[0] + L[-2])
for L in f:
    a = L[-2]
    print((L[0] + a) * int(a))
