from itertools import product
"""
product: 중복순열들의 값들을 출력한다.
"""

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1,6):
        for p in product(vowel, repeat = i):
            words.append("".join(p))

    words.sort()

    return words.index(word)+1
    
    