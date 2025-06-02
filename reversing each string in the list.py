a = []
for i in range(1,6):
    num=input("Enter the string: ")
    a.append(num)
b=[]
for i in a:
    word=i[::-1]
    b.append(word)
print(b)