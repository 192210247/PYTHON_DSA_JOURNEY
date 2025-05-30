a=input("Enter the word: ")
b=input("Enter the word: ")

a = a.replace(" ", "").lower()
b = b.replace(" ","").lower()

if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not anagram")
     




'''aa=set(a)
bb=set(b)
if aa==bb:
    print("It is anagram")
else:
    print("Its not a anagram")'''
