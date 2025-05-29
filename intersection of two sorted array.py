arr1=[]
arr2=[]
for element in range(1,6):
    num=int(input("Enter the element of array 1: "))
    arr1.append(num)
for element in range(1,6):
    num=int(input("Enter the element of array 2: "))
    arr2.append(num)

unique= set(arr1) |  set(arr2)
result=sorted(unique)
print("The Intersection of the two array is ",unique)
print("The Intersection of the two array is ",result)
