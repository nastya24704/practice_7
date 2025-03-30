result=[]
for i in range(100, 1000):
    if i % 17 == 0:
        result.append(i)
print(' '.join(map(str, result)))
print(len(result))
