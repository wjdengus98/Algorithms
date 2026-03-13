# 백준 28279번 (덱 2)
import sys
input = sys.stdin.readline  # 빠른 입력 

from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
    command = input().split()
    comm = command[0]  # 문자열 "1"~"8"

    if comm == '1':          
        dq.appendleft(int(command[1]))
    elif comm == '2':        
        dq.append(int(command[1]))
    elif comm == '3':        
        print(dq.popleft() if dq else -1)
    elif comm == '4':        
        print(dq.pop() if dq else -1)
    elif comm == '5':      
        print(len(dq))
    elif comm == '6':        
        print(0 if dq else 1)
    elif comm == '7':        
        print(dq[0] if dq else -1)
    elif comm == '8':        
        print(dq[-1] if dq else -1)