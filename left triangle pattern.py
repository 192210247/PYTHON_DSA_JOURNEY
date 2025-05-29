num = int(input("Enter the number of rows: "))  # Fixed typo in "numberr"
for i in range(num, 0, -1):  # Changed to include row 1 (changed from 1 to 0)
    # Print spaces
    for j in range(i):
        print(" ", end="")
    # Print stars
    for k in range(num - i + 1):
        if k == 0 or k == num - i or i == 1:  # Fixed condition for border stars
            print("*", end="")
        else:
            print(" ", end="")  # Print space for non-border positions
    print()  # Move to next line
