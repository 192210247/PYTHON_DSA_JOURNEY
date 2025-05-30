string=input("Enter the string:")
s_string=string.split()
count=[]
for word in s_string:
    length= len(word)
    count.append(length)
print(count)

for val in count:
    if val%2==0:
        print(val)