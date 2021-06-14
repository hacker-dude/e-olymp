input()
x = list(map(int, input().split()))
print(sum(x) - max(x) * x.count(max(x)))
