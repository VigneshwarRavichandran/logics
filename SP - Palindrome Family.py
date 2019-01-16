t=int(input())
while t>0:
    a=input()
    odd_str=""
    odd_count=0
    even_str=""
    even_count=0
    parent_count=0
   
    for i in range(0,len(a),2):
        odd_str=odd_str+a[i]
        
    for i in range(1,len(a),2):
        even_str=even_str+a[i]
        
    odd_temp = odd_str[::-1]
    if(odd_str==odd_temp):
        odd_count=odd_count+1
        
    even_temp = even_str[::-1]
    if(even_str==even_temp):
        even_count=even_count+1 
        
    rev_str = a[::-1]
    if(a==rev_str):
        parent_count=parent_count+1
         
    if(parent_count==1):
        print("PARENT")
    elif((odd_count==1)and(even_count==1)):
        print("TWIN")
    elif(odd_count==1):
        print("ODD")
    elif(even_count==1):
        print("EVEN")
    else:
        print("ALIEN")
    
    t=t-1  
        
         
