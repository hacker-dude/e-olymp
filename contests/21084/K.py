input()
list = list(map(int, input().split()))
min = min(list)
c = list.count(min)
while min in list:
    list.remove(min)
for i in "!" * c:
    list.insert(0, min)
print(*list)
