# 리스트의 탐색과 삭제
heroes = ["아이언맨", "토르", "헐크", "블랙위도우", "토르"]
n = heroes.index("헐크")
print(n)

# 삭제
heroes = ["아이언맨", "토르", "헐크", "블랙위도우", "토르"]
h = heroes.pop(1)  # pop은 인덱스로 제거
print(heroes)

heroes = ["아이언맨", "토르", "헐크", "블랙위도우", "토르"]
h = heroes.remove("헐크")  # remove는 데이터로 제거
print(heroes)