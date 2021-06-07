n = int(input())
list = map(int, input().split())
ans = []
for i in list:
    if i % 2 == 0: ans.append(i)

if len(ans) != 0:
    print(len(ans))
    print(*ans[::-1])
    exit()
print("NO")