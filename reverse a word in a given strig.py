'''words=input("Enter the string: ")
reverse=words[::-1]
print(reverse)'''

words=input("Enter the  string: ")
s_word=words.split()
rev=[]
for val in s_word:
    reverce=val[::-1]
    rev.append(reverce)
result=" ".join(rev)
print(str(result))