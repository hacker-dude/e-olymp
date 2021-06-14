<<<<<<< HEAD
l = int(input())
arr = list(map(int, input().split()))
g = [None] * l
g[0] = arr[0]
for i in range(1, l):
    g[(i + i) % l] = arr[i]
print(*g)
# incomplete
=======
# yoveli elementi win gadadis i- it da wreze midis
>>>>>>> 4711c3f188a0466b9b5c0081ab3d0b7da1b50351
