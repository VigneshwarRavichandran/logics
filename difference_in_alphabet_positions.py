input_data=list(map(str,input().split()))
str1=input_data[0]
str2=input_data[1]
sum=0
for i in range(0,len(str1)):
    a=ord(str1[i])
    b=ord(str2[i])
    c=b-a
    sum=sum+c
print(sum)
