#구구단1
 
t = int(input())
 
for i in range(t):
    num =int(input())
    flag = False
     
    for a in range(1,10):
        for b in range(1,10):
            if a * b == num:
                flag = True
                break
        if flag:
            break
         
                 
    if flag:
        print(f"#{i+1} Yes")
    else:
        print(f"#{i+1} No")