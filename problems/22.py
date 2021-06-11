def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


c = 0
n, m = map(int, input().split())
for i in range(n, m + 1):
    if is_prime(i) and is_prime(int(str(i)[::-1])):
        c += 1

print(c)
