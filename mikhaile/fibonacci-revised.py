total = 0
a, b = 1, 1
while b != 0:
    if b <= 4000000:
        print(a)
        a, b = b, a + b
        if b % 2 == 0:
            total += b 
    else:
        break
print("\n>>>", total)
