
def solution(phone_book):
    phone_book.sort() #정렬
    
    for i in range(len(phone_book)- 1): #정렬 후, 바로 뒤의 문자열이 앞의 문자열로 시작하는지 확인
        if phone_book[i+1].startswith(phone_book[i]): #startswith: 문자열이 특정 문자열로 시작하는지 확인
            return False #접두어면 False 반환
    return True   