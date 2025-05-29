num=int(input("Enter the numberr of rows: "))
for i in range(num,0,-1):
    for j in range(i):
        print(" ",end="")
    for k in range(num-i+1):
        if k==0 or k==num or i==1:
            print("* ",end="")
        else:
            print(" ",end="")
    print()