# 슬라이싱 - 한 번에 여러 개의 항목을 추출하는 기법

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sublist = numbers[2:7]
print("[2:7] : ", sublist)
prelist = numbers[:3]
print("[:3] : ", prelist)
postlist = numbers[3:]
print("[3:] : ", postlist)
alllist = numbers[:]
print("[:] : ", alllist)

list1 = numbers[::-1]
print("리스트-1 : ", list1)
