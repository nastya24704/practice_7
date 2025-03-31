n, k, r = map(int, input().split())
thread = n
days = 0
while thread < r:
    thread += n * 0.01 * k
    days += 1
print(days)
