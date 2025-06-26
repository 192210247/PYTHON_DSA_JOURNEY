list1 = [1, 3, 5, 7, 8, 0]
list2 = [4, 8, 9, 6, 5, 8]

# Combine and sort the two lists
combined = sorted(list1 + list2)

# Get the length of the combined list
n = len(combined)

# Find the median
if n % 2 == 1:
    # Odd number of elements: take middle element
    median = combined[n // 2]
else:
    # Even number of elements: average of two middle elements
    median = (combined[n // 2 - 1] + combined[n // 2]) // 2

print("Sorted Combined List:", combined)
print("Median:", median)
