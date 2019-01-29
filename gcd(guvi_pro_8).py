import math
ip1=list(map(int,input().split()))
n=ip1[0]
q=ip1[1]
arr=list(map(int,input().split()))
for i in range(0,q):
    ip2=list(map(int,input().split()))
    l=ip2[0]-1
    r=ip2[1]-1
    if(l>len(arr)):
        print(arr(r))
    elif(r>len(arr)):
        print(arr(l))
    else:
        res=math.gcd(arr[l],arr[r])
        print(res)
