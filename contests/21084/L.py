input()
list = list(map(int, input().split()))[::-1]
max = max(list)
c = list.count(max)
while max in list:
    list.remove(max)
for i in "!" * c:
    list.insert(0, max)
print(*list[::-1])
