n = int(input())
x = set()
for i in range(n):
    y = list(map(int, input().split()))[1:]
    for i in y:
        x.add(i)
print(len(x))
