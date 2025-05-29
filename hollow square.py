num=int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i==1 or i==num or j==1 or j==num:
            print("% ",end="")
        else:
            print("  ",end="")
    print()
