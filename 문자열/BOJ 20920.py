# 백준 알고리즘
# 20920번
# 영단어 암기는 괴로워
import sys
from collections import Counter
'''
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''

N,M = map(int, input().split())
words = []

#영단어 리스트에 저장
for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    
word_count = {} #단어 빈도 딕셔너리

for w in words:
    if w in word_count: # 딕셔너리에 들어 있다면 
        word_count[w] += 1 # 1 증가
    else: # 들어있지 않다면
        word_count[w] = 1 # 1 설정

# Counter를 써서 객체 단어와 단어 개수 객체 반환
word_dict = Counter(word_count)

#정렬(빈도, 길이, 사전)
sorted_word = sorted(
    word_dict.items(), key=lambda x: (-x[1],-len(x[0]), x[0])
)

# M보다 긴 단어만 출력
for w,c in sorted_word:
    if len(w) >= M:
        print(w)
