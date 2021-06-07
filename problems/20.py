n = int(input())
c = 0
while n > 0:
    m = n
    sum = 0
    while m > 0:
        sum += m % 10
        m /= 10
    n -= sum
    c += 1
print(c)
