word = "varshhaaaaa"
n = len(word)
count = 1  # the original string is always one valid option

i = 0
while i < n:
    j = i
    while j < n and word[j] == word[i]:
        j += 1

    group_len = j - i
    if group_len > 1:
        count += group_len - 1  # you can shorten the group in (len - 1) ways

    i = j  # move to next group

print(count)
