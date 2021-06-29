ans = []

pedals = list(map(int, input().split()))
backgear = list(map(int, input().split()))

for i in range(3):
    for j in range(7):
        ans.append([f'{pedals[i] / backgear[j]:.2f}', i + 1, j + 1])

for comb in sorted(ans, key=lambda x: x[0]):
    print(*comb)
