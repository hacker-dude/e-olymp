n = int(input())
list = map(int, input().split())
ans = []
for i in list:
    if i > 0: ans.append(i)

if len(ans) != 0:
    print(len(ans))
    print(*ans)
    exit()
print("NO")
