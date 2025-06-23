arr=[4,6,2,8,3,0,5,1]
for pos in range(len(arr)-1):
    min=pos
    for i in range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min = i
    arr[min],arr[pos]=arr[pos],arr[min]
print(arr)
