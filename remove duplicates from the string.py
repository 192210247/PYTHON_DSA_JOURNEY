words=input("Enter the string: ")
s_word=set()
word_list=[]
for word in words:
    if word not in s_word:
        s_word.add(word)
        word_list.append(word)
output="".join(s_word)
print(output)