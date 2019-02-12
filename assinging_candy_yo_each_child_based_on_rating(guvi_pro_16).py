n=int(input())
l=list(map(int,input().split()))
temp=[1]*n
count=n
while n>0:
    tcount=0
    for j in range(0,n):
        if j==0:
            if (l[j]>l[j+1])and(temp[j]<=temp[j+1]):
                count=count+1
                tcount=tcount+1
                temp[j]=temp[j]+1
        elif j==(n-1):
            if (l[j]>l[j-1])and(temp[j]<=temp[j-1]):
                count=count+1
                tcount=tcount+1
                temp[j]=temp[j]+1
        else:
            if (l[j]>l[j+1])and(temp[j]<=temp[j+1]):
                count=count+1
                tcount=tcount+1
                temp[j]=temp[j]+1
            if (l[j]>l[j-1])and(temp[j]<=temp[j-1]):
                count=count+1
                tcount=tcount+1
                temp[j]=temp[j]+1
    if tcount==0:
        break
print(count)
