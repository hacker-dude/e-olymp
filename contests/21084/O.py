n = int(input())
list = list(map(int, input().split()))
if n % 2 == 0:
    mid = (list[(n - 1) // 2] + list[n // 2])//2
else:
    mid = list[n // 2]

print(*[f - mid for f in list])
#incomplete
