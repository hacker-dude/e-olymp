n=int(input())
c=0
for i in range(1, n):
    if n//i == n%i:c+=1
print(c)