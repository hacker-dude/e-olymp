l = int(input())
g = []
arr = list(map(int, input().split()))[::-1]
for i in arr:
    if arr.count(i) > 1 and i not in g: g.append(i)

if len(g) != 0:
    print(*g[::-1])
    exit()
print("NO")
