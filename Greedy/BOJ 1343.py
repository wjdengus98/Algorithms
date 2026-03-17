# 백준
# 1343번
# 폴리노미오

board = input().split('.')

result = []
for chunk in board:
    if chunk == "":
        result.append("")
    else:
        cnt = len(chunk)
        temp = ""
        
        while cnt >= 4:
            cnt = cnt - 4
            temp += "AAAA"
        
        while cnt >= 2:
            cnt = cnt - 2
            temp += "BB"
        
        if cnt == 1:
            print(-1)
            exit()
            
        result.append(temp)

print(".".join(result))
