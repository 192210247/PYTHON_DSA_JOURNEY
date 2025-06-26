def maxproduct(num):
    n=len(num)
    arr=sorted(num)
    return arr[n-3]*arr[n-1]*arr[n-2]
num=[1,2,4,6,7,9,3,6]
print(maxproduct(num))