arr=[]
for i in range(1,6):
    num=int(input("Enter the elemnets of the array: "))
    arr.append(num)

minnum=min(arr)
maxnum=max(arr)

print("The minimum and maximum num of the array is ",minnum ,"and ",maxnum)