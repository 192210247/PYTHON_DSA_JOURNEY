arr=[6,8,4,2,9,1,3,7,5]
n=len(arr)
if(arr[0]>arr[1]):
    first= arr[0]
    second = arr[1]
else:
    first = arr[1]
    second= arr[0]
for i in range(0,n-1):
    if (arr[i]>first):
        second = first
        first = arr[i]
    if(arr[i]>second and second != first):
        second = arr[i]
print(second)

