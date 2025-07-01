arr = [5, 8, 9, 6, 3, 4, 1, 2, 7, 8, 0, 0, 0, -1, -2, -3, -4, -7, -8, -9, 9, 3]

even = 0
odd = 0
zero = 0
pos = 0
neg = 0

for num in arr:
    if num == 0:
        zero += 1
    elif num > 0:
        pos += 1
    elif num < 0:
        neg += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 13

print("Even:", even)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
