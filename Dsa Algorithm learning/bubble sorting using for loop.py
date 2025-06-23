arr=[1,3,7,0,5,8,4,9]
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:
            continue
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)