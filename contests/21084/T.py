l=int(input())
g = []
arr=list(map(int,input().split()))
for i in range(l-1):
    temp=[]
    for j in range(l-i):
        if arr[j]+1==arr[j+1]:
           temp.append(arr[j])
        else:
            g.append(temp)
            break
print(g)