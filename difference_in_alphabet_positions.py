input_data=list(map(str,input().split()))
str1=input_data[0]
str2=input_data[1]
length=0
l1=[]
l2=[]
sum=0
for i in range(0,len(str1)):
    a=ord(str1[i])
    l1.append(a)
for i in range(0,len(str2)):
    a=ord(str2[i])
    l2.append(a)
if(len(str1)<len(str2)):
    temp=len(str2)-len(str1)
    t=[96]*temp
    l1=l1+t
if(len(str1)>len(str2)):
    temp=len(str1)-len(str2)
    t=[96]*temp
    l2=l2+t
for i in range(0,len(l1)):
    c=l2[i]-l1[i]
    sum=sum+c
print(sum)
