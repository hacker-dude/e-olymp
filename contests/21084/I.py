input()
list = list(map(int, input().split()))
indM = list.index(min(list))
list[0], list[indM] = list[indM], list[0]
print(*list)
