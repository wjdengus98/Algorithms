#  백준 베스트셀러
N = int(input())
book_dict = {}

for _ in range(N):
    book = input()
    
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

# 판매량 내림차순 정렬, 사전순 오름차순 x[1]: 판매량, x[0]: 이름
sorted_book = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))

print(sorted_book[0][0])