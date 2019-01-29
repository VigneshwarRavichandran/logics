s=input()
res=[]
even_count=0
odd_count=0
count=0
for i in range(0,len(s)):
    val=int(s[i])
    if((val%2==0)and(count==0)):
        count=count+1
        even_count=1
        ocount=0
    elif((val%2!=0)and(even_count==1)and(count>0)):
        count=count+1
        odd_count=1
        even_count=0
        print(val," ",count)
    elif((val%2==0)and(odd_count==1)and(count>0)):
        count=count+1
        odd_count=0
        even_count=1
    else:
        res.append(count)
        count=0
        even_count=0
        odd_count=0
    if(i==len(s)-1):
        res.append(count)
print(res)
