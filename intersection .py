arr1=[]
arr2=[]
for element in range(1,6):
    num=int(input("Enter the number"))
    arr1.append(num)
for element in range(1,6):
    num=int(input("Enter the number"))
    arr2.append(num)

result= set(arr1) & set(arr2)  
print("The intersection of the two arrays is ", result)