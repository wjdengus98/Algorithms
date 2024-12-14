#스택2

import sys

N = int(sys.stdin.readline())  # 명령의 수 입력 받기
ST = []  # 스택 초기화

for _ in range(N):  # 5가지의 명령에 대해서 코드 작성
    op = sys.stdin.readline().split()  # 명령 입력
    if op[0] == '1':
        ST.append(int(op[-1]))
    elif op[0] == '2':
        print(ST.pop() if ST else -1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        print(0 if ST else 1)
    elif op[0] == '5':
        print(ST[-1] if ST else -1)
