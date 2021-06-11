n = int(input())
c = 0
while n != 1:
    if not n&1:
        n //= 2
        c += 1
    else:
        n += 1
        c += 1
print(c)
