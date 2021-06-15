input()
x = list(map(int, input().split()))
print(*[f + 2 if f >= 0 else f for f in x])
