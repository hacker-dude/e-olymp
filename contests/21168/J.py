n = int(input())
x = list(map(int, input().split()))
for i in range(n - 1):
    x.append(2 * min(x[i], x[i + 1]))
print(2 * sorted(x)[-2])
 # 7%