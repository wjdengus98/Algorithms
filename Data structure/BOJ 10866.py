# 백준 10866번
# 덱

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

dq = deque()
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(1 if not dq else 0)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)