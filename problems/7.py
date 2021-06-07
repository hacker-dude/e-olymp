roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def sumr(x):
    sum = 0
    for i in x:
        sum += roman[i]
    return sum


sum = 0
for i in input().split('+'):
    sum += sumr(i)
print(sum)