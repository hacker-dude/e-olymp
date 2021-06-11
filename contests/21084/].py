l = int(input())
arr = list(map(int, input().split()))
x = set()
for i in arr:
    x.add(i)
print(*sorted(x))
