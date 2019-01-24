#Input : MAGMA GEMSTONE  Output : 8
#Input : JOKER JOKER  Output : 0
n=input()
m=input()
count=abs(len(n)-len(m))
if(len(n)>=len(m)):
    for i in range(0,len(m)):
        if(n[i]!=m[i]):
            count=count+1
else:
    for i in range(0,len(n)):
        if(n[i]!=m[i]):
            count=count+1
print(count)
