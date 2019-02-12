ip1=list(map(int,input().split()))
n=ip1[0]
k=ip1[1]
arr=list(map(int,input().split()))
count=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(arr[i]+arr[j])==k:
            count=count+1
if count==0:
    print("no")
else:
    print("yes")
