# 어떤 자연수 n이 주어졌을 때, n을 두 개 이상의 자연수의 합으로 나타내는 방법은 여러 가지가 있다. 이때 그 자연수들의 곱이 최대가 되도록 나누고자 한다.

# 예를 들어 n = 8인 경우:

# 1+1+1+1+1+1+1+1 = 8, 곱 = 1
# 2+2+4 = 8, 곱 = 16
# 3+3+2 = 8, 곱 = 18
# 4+4 = 8, 곱 = 16
# ...

# 이 중 곱이 최대인 경우는 3+3+2이며, 이때 곱은 3 × 3 × 2 = 18이다.

# 단, 두 자연수 이상으로 나누어야 한다. (n 자체를 그대로 두는 것은 허용되지 않음)

# 예를 들어 n = 3인 경우, 가능한 나눔은 1+2 또는 1+1+1뿐이므로, 최대곱은 1×2 = 2이다.

# 제한사항
# n은 2 이상 100 이하의 자연수이다.
# 예시
# n	answer	설명
# 2	1	1+1
# 3	2	1+2
# 8	18	3+3+2
# 10	36	3+3+4

n = 8
def solution(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        quotient,remainder = divmod(n,3)
        if remainder == 0:
            max_val = (3 ** quotient)
        elif remainder == 1:
            max_val = (3 ** (quotient - 1)) * 4
        else:
            max_val = (3 ** quotient) * remainder
        return max_val

if __name__ == "__main__":
    print(solution(n))