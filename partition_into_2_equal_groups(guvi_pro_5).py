ip=list(map(int,input().split()))
n=ip[0]
a=ip[1]
b=ip[2]
res=0
check=0
while res<n:
    res=res+a+b
    if(res==n):
        check=1
        break
    else:
        check=0
if(check==1):
    print("YES")
else:
    print("NO")
