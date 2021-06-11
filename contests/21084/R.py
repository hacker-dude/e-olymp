l = int(input())
arr = list(map(int, input().split()))
g = [None] * l
g[0] = arr[0]
for i in range(1, l):
    g[(i + i) % l] = arr[i]
print(*g)
# incomplete
