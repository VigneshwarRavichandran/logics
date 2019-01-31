ip1=list(map(int,input().split()))
n=ip1[0]
q=ip1[1]
arr=list(map(int,input().split()))
for i in range(0,q):
    ip=list(map(int,input().split()))
    u=ip[0]-1
    v=ip[1]
    sum=0
    for i in range(u,v):
        sum=sum+arr[i]
    print(sum)
