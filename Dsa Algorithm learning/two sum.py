num =[1,2,3,4,5,6,7]
target = int(input("Enter the target value: "))

for  i in range(len(num)):
    for j in range(i+1,len(num)) :
        if num[i]+num[j] == target:
            print(i,j)