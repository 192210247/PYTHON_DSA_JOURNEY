
list1=[1,2,3,4,5,6,7,8,9,0]
list1.sort()
target = int(input("enter the target: "))
l=0
r=len(list1)-1
while l<=r:
    mid = (l+r)//2
    if list1[mid] == target:
        print(mid)
        break
    elif  list1[mid]> target:
        r=mid-1
    elif  list1[mid]<target:
        l=mid+1
    else:
         print("The Target not found")