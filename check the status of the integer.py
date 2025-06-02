def posneg(x,y):
    if x>=0 and y>=0:
        return True
    else:
        return False

a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
result=posneg(a,b)
print(result)