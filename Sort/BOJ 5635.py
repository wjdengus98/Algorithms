#백준 5635번

n = int(input()) #학생의 수

info = [] #학생들의 정보를 저장할 리스트

for i in range(n):
    st,dd,mm,yyyy = input().split()
    info.append((st,int(dd),int(mm),int(yyyy)))


def cmp(person): #비교함수
    st,dd,mm,yyyy = person
    return (yyyy,mm,dd)


info.sort(key=cmp) #연도,월,일 순으로 정렬

print(info[-1][0]) #나이가 가장 적은 사람
print(info[0][0]) #나이가 가장 많은 사람