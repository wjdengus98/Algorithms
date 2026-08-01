# 문제

# 두 문자열 line1, line2가 주어진다. line1은 원본 문자열이고, line2는 그 안에서 찾고자 하는 패턴이다.

# line1의 문자들을 순서를 바꾸지 않고 그대로 두되, 일부 자리에 임의의 문자열(공백 포함, 아무 문자나 가능)을 끼워 넣은 것으로 간주했을 때, 그 공백들을 제외하고 남은 글자들만 이었을 때 line2와 정확히 일치하는 형태를 만들 수 있다.

# 예를 들어 line1 = "aabbcc", line2 = "abc"인 경우, 다음과 같은 형태로 line2를 만들 수 있다.

# a_b_c
# _a_b_c_

# (밑줄 _은 임의의 문자열이 들어갈 수 있는 자리를 의미한다.)

# 이때 서로 겹치지 않게(같은 글자를 재사용하지 않고) 이런 형태를 최대 몇 번 만들 수 있는지 구하고자 한다.

# line1 = "aabbcc"인 경우, a가 2개, b가 2개, c가 2개 있으므로 서로 겹치지 않는 두 묶음 (a, b, c)와 (a, b, c)를 각각 만들 수 있어 최대 2번까지 만들 수 있다.

# 제한사항
# line1, line2는 알파벳 소문자로만 이루어진 문자열이다.
# line2의 길이는 line1의 길이보다 작거나 같다.
# line2 내부에는 같은 글자가 중복되지 않는다고 가정한다.
# 예시
# line1	line2	answer	설명
# "aabbcc"	"abc"	2	(a,b,c) 묶음 2개
# "abcabc"	"abc"	2	(a,b,c) 묶음 2개
# "aaabbbccc"	"abc"	3	(a,b,c) 묶음 3개
# "abccba"	"abc"	1	뒤쪽 "cba"는 순서가 반대라 사용 불가
# "xyz"	"abc"	0	필요한 글자가 아예 없음


def solution(line1,line2):
    counts = [0] * len(line2) # line2의 글자를 몇 번 완성했는 지
    
    for ch in line1:
        for i,target_ch in enumerate(line2):
            if ch == target_ch:
                if i == 0: # 첫 글자는 무조건 시작 후보 가능
                    counts[i] += 1
                else:
                    # i번째 글자는 반드시 i-1번째 글자 뒤에 와야하고
                    # 갯수가 적을 때만 카운트 -> 그래야 앞에 것이 완성됐다는 의미이므로.
                    if counts[i] < counts[i-1]:
                        counts[i] += 1
                break
    
    return counts[len(line2) - 1]



if __name__ == "__main__":
    print(solution("aabbcc", "abc"))
    print(solution("abcabc", "abc"))
    print(solution("aaabbbccc", "abc"))
    print(solution("abccba", "abc"))
    print(solution("xyz", "abc"))