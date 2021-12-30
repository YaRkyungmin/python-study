# autor: YaRkyungmin
# 2021-12-29
# Python DataType List

# list datatype(sequence)
'''
sequence
중복
수정
삭제
'''
a = []
b = list()

## list indexing
list_index = [1,2,'3','4',5.0]
print(str(list_index[1])+list_index[3])

## list slicing(=범위 지정) -> 리스트를 반환
list_slice = [1,2,3,4,5]
print(list_slice[:3])

## list operator -> 리스트를 반환
list1 = [1,2,3]
list2 = [4,5,'6']
print(list1 + list2)
print(list1 * 3)

## compare list
list_compare = [1,2,3,4,5,6,7,8]
print(list_compare == list_compare[:3] + list_compare[3:])

## list identity(id)
list_id = [1,2,3]
temp = list_id
print(id(temp))
print(id(list_id))

## list 수정, 삭제
list_edit = [1,2,3,4]
list_edit[1:2] = ['a','b','c']
print(list_edit)

list_edit = [1,2,3,4]
list_edit[1:6] = ['a','b','c']
print(list_edit)

list_edit = [1,2,3,4]
list_edit[1:2] = [['a','b','c']]
print(list_edit)

list_edit = [1,2,3,4]
list_edit[1] = ['a','b','c']
print(list_edit)

list_edit = [1,2,3,4]
del list_edit[2]
print(list_edit)

## list function (함수를 반영하면 부모 list가 바로 반영된다)
'''
append
pop 인덱스 위치를 지정 삭제(스택-LIFO)
remove 특정 값 삭제(한번만 제거)
sort (시간복잡도가 큼)
reverse 데이터를 반대로 (시간복잡도가 큼)
count 특정값의 갯수를 반환
index
insert 위치 지정 삽입
extend 리스트를 연장 (slicing과 마찬가지로 범위에 순서대로 넣어줌, 통으로 들어가지 않음)
'''
list_fu = [1,2,3,4,0]
list_fu.append(5)
print(list_fu)

list_fu.pop()
print(list_fu)

list_fu.sort()
print(list_fu)

list_fu.reverse()
print(list_fu)

print(list_fu.index(2))

list_fu.insert(2,'insert')
print(list_fu)

list_fu.append(0)
list_fu.append(0)
list_fu.remove('insert')
list_fu.remove(0) #0을 한번만 제거한다.
print(list_fu)

print(list_fu.count(0))

list_fu.extend(['extend',0])
print(list_fu)

## list 반복문
while list_fu: #비어있을때까지 실행
    data = list_fu.pop()
    print(data)

### enumerate - for문에서 index변수 없이 실행가능하게 해줌
list_enumer = ['a','b','c']
for element in enumerate(list_enumer):
    print(element) #tuple 형태로 반환 해준다

for idx,element in enumerate(list_enumer):
    print(idx,element) #index변수를 지정해줄때

for idx,element in enumerate(list_enumer, start=1):
    print(idx,element) #index를 1부터 시작할때