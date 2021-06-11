from datetime import date

n = int(input())
c = 0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b):
        for z in range(1, 13):
            if date(j, z, 13).weekday() == 5: c += 1
print(c-1)
