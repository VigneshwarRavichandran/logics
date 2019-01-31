n=int(input())
count=0
for i in range(1,n):
    for j in range(i+1,n+1):
        count=count+1
print(count)      
