s=input()
invalid_check=0
nest_count=[0]
count=0
open_bracket=0
close_bracket=0
for i in range(0,len(s)):
    if(s[i]=="("):
        open_bracket=open_bracket+1
        count=0
    elif(s[i]==")"):
        close_bracket=close_bracket+1
        nest_count.append(count)
        count=0
    else:
        count=count+1
    if(close_bracket>open_bracket):
        invalid_check=1
        break;
if invalid_check==0:
    if(open_bracket==close_bracket):
        print(max(nest_count))
    else:
        print("-1")
else:
    print("-1")
