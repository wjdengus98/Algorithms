n = int(input())

for five in range(n // 5, -1, -1):
    rest = n - (5 * five)
    if rest % 2 == 0:
        two = rest // 2
        print(five + two)
        break
else:
    print(-1)