input()
list = list(map(int, input().split()))
# print(*[f - 7 if f > 0 else f + 5 for f in list])
from statistics import mean

print(mean(list))

# incomplete
