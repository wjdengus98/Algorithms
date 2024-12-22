#팔씨름

n = int(input())

for i in range(n):
    games = input()
    is_win = 0
    
    round = len(games)
    
    for j in range(round):
        if games[j] == 'o':
            is_win += 1
    extra_win = 15 - round
    is_win += extra_win
    
    if is_win >= 8:        
         print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
    
    

