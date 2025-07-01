arr=[10,20,30,40,50]
n=len(arr)
sums,count=0,0
for i in range(0,n):
    sums += arr[i]
average = sums /n
print(average)
for i in range(0,n):
    if  arr[i] > average:
        count +=1
print(count)