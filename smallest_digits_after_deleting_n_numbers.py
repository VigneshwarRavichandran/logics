input_data=list(map(int,input().split()))
s=str(input_data[0])
s_len=len(s)
temp=len(s)
n=input_data[1]
l=[]
if n>0:
    for i in range(0,n):
        if i==0:
            for j in range(0,temp):
                var=s[:j] + s[(j+1):]
                l.append(var)
        if i>0:
            for j in range(0,temp):
                temp_val=((i-1)*temp)+j
                temp_var=l[temp_val]
                for k in range(0,s_len):
                    var=temp_var[:k] + temp_var[(k+1):]
                    l.append(var)
        s_len=s_len-1
    print(min(l))
else:
    print(s)
