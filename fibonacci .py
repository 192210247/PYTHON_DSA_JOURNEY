def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fibonacci(num-1)+fibonacci(num=2)

result=fibonacci()
print(result)