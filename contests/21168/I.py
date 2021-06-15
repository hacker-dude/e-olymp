n = int(input())
x = sorted(list(map(int, input().split())))
s = 0
c = 0
for i in range(n):
    s += x[i]
    c += s
print(c-1)
# incomplete
