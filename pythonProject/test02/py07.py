# 튜플 / 딕셔너리 / 세트
# 튜플 - 변경 불가
fruits = ("apple", "banana", "grape")
print(fruits)
print(fruits[0])
for f in fruits :
    print(f, end=", ")

# 튜플을 리스트로
myTuple=(1,2,3,4)
myList=list(myTuple)
print()
print(myList)

# 딕셔너리 - 키/값

# 세트 - 중복 불가
numbers = {1,2,3}
print("set=", numbers)

numbers1 = set([1,2,2,3,4,5,5])
print("set=", numbers1)

numbers1.add(7)
print("set=", numbers1)

# 세트 함축 연산
aList = [1,2,3,4,5,1,2]
result = {x for x in aList if x % 2 == 0}
print("x=%2", result)

# 세트 - 교집합 / 합집합 / 차집합
a = {"apple", "banana", "grape" }
b = {"apple", "banana", "kiwi" }
c = a | b
d = a & b
e = a - b
print("합집합", c)
print("교집합", d)
print("차집합", e)