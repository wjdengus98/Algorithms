#백준 바닥장식
badak = []
n,m = map(int,input().split())

for i in range(n):
    badak.append(list(map(str,input())))


def dfs(x, y, char):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if badak[x][y] == char:
        badak[x][y] = 1  # 방문했다는 표식
        
        if char == '-':
            dfs(x, y + 1, char)  # '-'일 때는 가로 방향으로 탐색
        elif char == '|':
            dfs(x + 1, y, char)  # '|'일 때는 세로 방향으로 탐색
            
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if badak[i][j] == '-':
            if dfs(i, j, '-'):
                result += 1
        elif badak[i][j] == '|':
            if dfs(i, j, '|'):
                result += 1

print(result)


    







