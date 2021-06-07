n = int(input())
list = list(map(int, input().split()))
print(*[list[0]]+[list[f] - list[f - 1] for f in range(1, n)])
