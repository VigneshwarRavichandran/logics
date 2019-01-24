arr=list(map(str, input().strip().split()))
res=[0]*52
count=0
for i in range(0,len(arr)):
    val=set(arr[i])
    convert_val=list(val)
    for j in range(0,len(convert_val)):
        temp=ord(convert_val[j])
        if temp<91:
            res[temp-65]=res[temp-65]+1
        if temp>96:
            res[temp-71]=res[temp-71]+1
res.sort(reverse = True)
for i in range(0,len(res)):
    if(res[i]==len(arr)):
        count=count+1
    else:
        break
print(count)
