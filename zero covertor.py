def pos(n):
    while n>=0:
        print(n,end=" ")
        n-=1
def neg(n):
    while n<=0:
        print(n,end=" ")
        n+=1
num=int(input("Enter the number: "))
pos(num)
neg(num)