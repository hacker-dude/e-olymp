input()
list = list(map(int, input().split()))
indM = list[::-1].index(max(list))
list[-1], list[-indM - 1] = list[-indM - 1], list[-1]
print(*list)
