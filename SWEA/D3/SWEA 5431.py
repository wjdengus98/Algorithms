T = int(input())

for i in range(T):
    n, k = map(int, input().split())
    submits = list(map(int, input().split()))
    
    players = [i for i in range(1, n+1)]
    no_submit = []

    for player in players:
        if player not in submits:
            no_submit.append(player)

    print(f"#{i+1}", *no_submit)
