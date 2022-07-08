# 슬라이스 응용

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ['white', 'blue', 'red']  # 범위 삽입
print(lst)


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst1[::2] = [99, 99, 99, 99]  # 단계별 삽입
print(lst1)

lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2[:] = []  # 모든 리스트 공백으로 처리
print(lst2)

# 출력식 : 입력리스트
squares = [x * x for x in range(10)]
print("=>", squares)

# 출력식 : 입력리스트 : 조건식
squares = [x * x for x in range(10) if x %2 == 0]
print("=>", squares)