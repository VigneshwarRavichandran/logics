n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(0,n):
    s=bin(arr[i])
    s=str(s[2:])
    one_n=0
    for j in range(0,len(s)):
                   if(s[j]=='1'):
                       one_n=one_n+1
    ans.append([arr[i],s,one_n])
ans.sort(key = lambda x: x[0],reverse=True)
ans.sort(key = lambda x: x[2],reverse=True)
for num,binary_num,one_num in ans:
    print(num)
