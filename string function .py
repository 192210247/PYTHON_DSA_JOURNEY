string = input("Enter the string : ")
original = string.lower()
if original.startswith("good") and original.endswith("good"):
    print("Correct")
else:
    print("not correct")


word=input("enter the word: ")
reverse=word[::-1]
print(reverse)
