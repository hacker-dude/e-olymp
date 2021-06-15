x = []
for i in range(int(input())):
    x += input(),

t = []
for i in set(x):
    t += (x.count(i), i),

print(*max(t)[::-1])
