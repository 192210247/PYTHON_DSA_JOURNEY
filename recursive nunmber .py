def natural_num(num):
    if num==0:
        return 0
    return num+ natural_num(num-1)
result=natural_num(10)
print(result)