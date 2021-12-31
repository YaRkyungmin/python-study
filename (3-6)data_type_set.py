# autor: YaRkyungmin
# 2021-12-31
# Python DataType Set

# set datatype
'''
순서 X
중복 X
추가 O
삭제 O
'''
a = set()
b = set([1,2,3,4,4,4,4]) #중복 허용 X
c = set([1,2,'3','4',(1,2)])
d = {'s','e','t','s'}
print(b)
print(c)

## set -> tuple type casting
t = tuple(b)
print(type(t),t)
print(t[0],t[1:3])

## set -> list type casting
l = list(b)
print(l)

## set len
print(len(a))
print(len(b))
print(len(c))

## set operator & function
'''
& 교집합
intersection 교집합
| 합집합
union 합집합
- 차집합
difference 차집합

isdisjoint 중복 원소 확인 - 공통 원소가 있으면 False를 반환, 공통 원소가 없으면 True
A issubset B (A가 B의 부분집합 인가?)부분 집합 확인 - bool 값을 반환
A issuperset B (A가 B를 포함하는 집합인가?)부분 집합 확인 - bool 값을 반환
'''

set_op = set([1,2,3,4,5,6])
set_op2 = set([4,5,6,7,8,9])

print(set_op & set_op2) 
print(set_op.intersection(set_op2))

print(set_op|set_op2)
print(set_op.union(set_op2))

print(set_op - set_op2)
print(set_op.difference(set_op2))

print(set_op.isdisjoint(set_op2))

print(set_op.issubset(set_op2))

## set edit & delete
set_edit = set([1,2,3,4,5])
set_edit.add(6)
print(set_edit)

set_edit.remove(1) 
print(set_edit)
###set_edit.remove(7) #없는값을 입력하면 key error 발생

set_edit.discard(3)
print(set_edit)
set_edit.discard(8) #없는값을 입력해도 key error가 발생 안함 (예외 발생 안함)
print(set_edit)

set_edit.clear()
print(set_edit)