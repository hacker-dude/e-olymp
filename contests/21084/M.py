input()
list = list(map(int, input().split()))
min = 101
for i in list:
    if i / 2 < min: min = i//2
print(*[f - min for f in list])

