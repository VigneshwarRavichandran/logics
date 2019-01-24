a=int(input())
s=list(map(str,input().split()))
res=[s[0]]
for i in range(0,len(s)-1):
    val=''
    s1_temp=res[i]
    s2_temp=s[i+1]
    for j in range(0,len(s1_temp)):
        if(s1_temp[j]==s2_temp[j]):
            val=val+s1_temp[j]
        else:
            break
    res.append(val)
print(res[len(res)-1])
