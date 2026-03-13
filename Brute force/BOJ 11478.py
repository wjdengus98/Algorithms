# 백준 11478번
# 11478번: 서로 다른 부분 문자열의 개수
# 문제풀이 Tip: 이중 for문으로 모든 부분 문자열을 생성해 Set에 담은 후 길이 출력 

words = input()

words_set = set()
l = len(words)

for i in range(l):
    
    for j in range(l - i):
        word = words[i:j+i+1]
        words_set.add(word)

print(len(words_set))