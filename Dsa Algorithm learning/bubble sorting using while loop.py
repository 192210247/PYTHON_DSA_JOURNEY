arr=[2,6,9,3,5,0,1,8]
while True:
    a=True
    for j in range(len(arr)-1):
        if arr[j]<arr[j+1]:
            continue
        elif arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            a=False
    if a:
        break
print(arr)
        