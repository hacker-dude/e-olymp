n = int(input())
list = list(map(int, input().split()))
print(len([*list[1::2]]))
print(*list[1::2])
# incomplete
