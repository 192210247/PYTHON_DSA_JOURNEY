list1 = [1,2,3,4,5,6,7,8,9,0]
target = int (input("Enter the target value :   "))
for i in range(len(list1)):
    if list1[i] == target:
        print(i)