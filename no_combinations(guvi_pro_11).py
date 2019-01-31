n=int(input())
count=[]
for i in range(1,n):
    for j in range(i+1,n+1):
        count.append([i,j])
print(len(count))       
