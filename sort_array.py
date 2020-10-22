n=int(input())
arr=list(map(int,input().split()))
z=[]
y=[]
for i in range(n):
    if arr[i]%2==0:
        z.append(arr[i])
    else:
        y.append(arr[i])
#print(z)
#print(y)
print(z+y)
        
