arr=[4,5,3,7,9,6,1,2,0]
for i in range(1,len(arr)):
    cur_pos = arr[i]
    j=i-1

    while j>=0 and cur_pos<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=cur_pos
print(arr)