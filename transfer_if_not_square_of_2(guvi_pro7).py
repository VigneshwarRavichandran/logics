n=int(input())
count=0
i=1
while i<n:
    if((2**i)==n):
        count=0
        break;
    if((2**i)>n):
        temp=i-1
        count=n-(2**temp)
        break;
    i=i+1
print(count)
