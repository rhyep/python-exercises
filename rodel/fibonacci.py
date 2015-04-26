# fibonacci.py

count = 0
prev = 0
sum = 0
while count < 3:
    if sum == 1:
        print(sum + count)
    else:
        print(count)
    sum = count + prev
    prev = count
    count += 1
