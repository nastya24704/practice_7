word = input()
result=''
for i in range(2, len(word), 3):
    result += word[i]
print(result)
