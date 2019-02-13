ip=input()
l=[]
check=0
for i in range(2,ip+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        l.append(i)
for i in range(0,len(l)-1):
    for j in range(i,len(l)):
        if((l[i]+l[j])==ip):
            check=check+1
if check==0:
    print("False")
else:
    print("True")
