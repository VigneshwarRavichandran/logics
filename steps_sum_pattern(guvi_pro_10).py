n=int(input())
s=list(map(int,input().split()))
count=0
for i in range(1,n):
    if(s[i]>s[i-1]):
        for j in range(0,i):
            count=count+s[j]
print(count)
