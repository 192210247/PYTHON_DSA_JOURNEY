def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
        
while True:
    starting =input("Enter the number or stop to end: ")
    if starting == 'stop':
        break

    if starting.isdigit():
        num=int(starting)
        for i in range(num+1):
             print(fibonacci(i),end=" ")