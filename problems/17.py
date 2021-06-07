a, b, c = map(int, input().split())
x1, y1, x2, y2, z2 = map(int, input().split())
hyp = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + z2 ** 2) ** .5
ans = hyp**2 - (c-z2)**2
print(f"{ans+(c-z2):.2f}")
