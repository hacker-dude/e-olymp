n, a, b, c, d = list(map(int, input().split()))
nums = [*range(1, n+1)]

nums[a-1:b] = nums[a-1:b][::-1]
nums[c-1:d] = nums[c-1:d][::-1]

print(*nums)
