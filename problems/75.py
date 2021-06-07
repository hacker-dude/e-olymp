a, m = map(int, input().split())
c = 0
while a * 2 <= m:
    a += 1
    m -= a
    c += 1
print(c + 1)
