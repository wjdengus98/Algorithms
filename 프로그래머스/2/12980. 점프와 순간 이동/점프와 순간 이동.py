def solution(n):
    ans = 0
    while n > 0:
        ans += n % 2   # 홀수면 점프 1회
        n //= 2        # 짝수면 순간이동
    return ans