# 백준 알고리즘 - 단어 정렬 (1181)
# 문제: https://www.acmicpc.net/problem/1181

n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())

# 리스트로 변환 후 정렬: (길이, 단어) 순
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
