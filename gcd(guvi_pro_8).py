import math
ip1=list(map(int,input().split()))
n=ip1[0]
q=ip1[1]
arr=list(map(int,input().split()))
for i in range(0,q):
    ip2=list(map(int,input().split()))
    l=ip2[0]
    r=ip2[1]
    if(l==r):
        temp_res=math.gcd(l,r)
        res=temp_res*arr[0]
        print(res)
    else:
        res=math.gcd(l,r)
        print(res)
