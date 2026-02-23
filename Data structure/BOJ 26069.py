N = int(input())

dancer = {'ChongChong'}

for _ in range(N):
    a,b = input().split()
    
    # Chongchong이 댄서면 옆 사람을 댄서그룹 추가    
    if a in dancer:
        dancer.add(b)
    elif b in dancer:
        dancer.add(a)
        
print(len(dancer))