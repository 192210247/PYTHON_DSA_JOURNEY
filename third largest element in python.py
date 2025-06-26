def thirdlargestelement(num):
    arr=sorted(num)
    n=len(num)
    for i in range(n-3,-1,-1):
        if arr[i]!=arr[n-1]:
            return arr[n-3]
        return -1

num=[14,5,48,6,7,25,91,63]
print(thirdlargestelement(num))

