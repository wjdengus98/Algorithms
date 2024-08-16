#FBI
FBI_list = []
name =''
for i in range(5):
    name = input()
    
    if 'FBI' in name:
        FBI_list.append(i+1)

if len(FBI_list) == 0:
    print('HE GOT AWAY!')
else:
    print(*FBI_list)
