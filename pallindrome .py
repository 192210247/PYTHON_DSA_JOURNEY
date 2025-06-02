s=input("Enter the word: ")
found=False
for i in range ( len(s)):
    temp=(s[:i]+s[i+1:])
    if temp == temp[::-1]:
        found=True
        break
if(found==True):
    print(temp)