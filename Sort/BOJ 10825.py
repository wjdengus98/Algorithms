# 백준 알고리즘 - 10825번
# 국영수
# https://www.acmicpc.net/problem/10825

import sys

n = int(input())
students = []

for _ in range(n):
    name,kor,eng,math = sys.stdin.readline().split()
    kor,eng,math = int(kor), int(eng),int(math)
    students.append([name,kor,eng,math])

# 점수는 int, 이름은 str
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])