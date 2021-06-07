n = input()
c = 0
while n != n[::-1]:
    n = str(int(n) + int(n[::-1]))
    c += 1
print(c)
