#백준 9655 돌게임
#다이나믹 프로그래밍

n = int(input())
d = [-1]*1001

d[1] = 1 #상근이가 이김
d[2] = 0 #창용이가 이김
d[3] = 1 #상근이가 이김

# win[n]일때 승자를 알고 싶을 때, win[n-1],win[n-3] 이 승자와 반대 사람이 이긴다.


for i in range(4,n+1):
    if (d[i-1] == 1 or d[i-3] == 1):    
        d[i] = 0
    else:
        d[i] = 1

if d[n] == 1:
    print("SK")
else:
    print("CY")