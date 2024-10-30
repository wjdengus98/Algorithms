#거꾸로 출력해 보아요 - swea
'''
입력
8

출력
8 7 6 5 4 3 2 1 0
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
nums_list = []
for test_case in range(T, -1,-1):
    # ///////////////////////////////////////////////////////////////////////////////////
 	nums_list.append(test_case)

for num in nums_list:
    print(num, end = " ")