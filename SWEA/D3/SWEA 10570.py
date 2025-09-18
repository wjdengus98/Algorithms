def is_palindrome(n):
    """숫자가 팰린드롬인지 확인하는 함수"""
    s = str(n)
    return s == s[::-1]

def is_perfect_square(n):
    """완전제곱수인지 확인하는 함수"""
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def count_square_palindromes(A, B):
    """A 이상 B 이하 범위에서 제곱 팰린드롬 수의 개수를 구하는 함수"""
    count = 0
    
    for n in range(A, B + 1):
        # n이 팰린드롬인지 먼저 확인 (더 효율적)
        if is_palindrome(n):
            # n이 완전제곱수인지 확인
            if is_perfect_square(n):
                sqrt_n = int(n ** 0.5)
                # √n도 팰린드롬인지 확인
                if is_palindrome(sqrt_n):
                    count += 1
    
    return count

# 입력 처리
TC = int(input())

for case in range(1, TC + 1):
    A, B = map(int, input().split())
    result = count_square_palindromes(A, B)
    print(f"#{case} {result}")