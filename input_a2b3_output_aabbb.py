s=input()
num_list=[]
alpha_list=[]
num=''
for i in range(0,len(s)):
    if(s[i].isalpha()):
        alpha_list.append(s[i])
        if(i>0):
            num_list.append(num)
        num=''
    if(s[i].isnumeric()):
        num=num+s[i]
num_list.append(num)
for i in range(0,len(alpha_list)):
    n=int(num_list[i])
    print(alpha_list[i]*n,end="")
