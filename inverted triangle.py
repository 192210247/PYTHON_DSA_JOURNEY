num= int(input("Enter the number of row: "))
for i in range(1,num+1):
    for j in range(num-i+1):
        print("* ",end="")
    print()