#팩토리얼 0의 개수
from math import factorial

n = int(input())

result = factorial(n)

result2 = str(result)

#print(result2)

cnt=0

for i in range(len(result2)- 1,-1,-1):
        if result2[i] == '0':
            cnt += 1
        else:
            break
        
print(cnt) 