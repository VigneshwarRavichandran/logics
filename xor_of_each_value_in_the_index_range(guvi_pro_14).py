ip1=list(map(int,input().split()))
n=ip1[0]
q=ip1[1]
arr=list(map(int,input().split()))
for i in range(0,q):
    ip=list(map(int,input().split()))
    u=ip[0]-1
    v=ip[1]
    temp=0
    for j in range(u,v):
        res=temp^arr[j]
        temp=res
    print(temp)
