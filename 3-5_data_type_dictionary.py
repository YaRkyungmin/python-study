# autor: YaRkyungmin
# 2021-12-30
# Python DataType Dictionary

# dictionary datatype (JSON과 비슷)
'''
순서 X
키 중복 X
수정 O
삭제 O
'''
a = {'name':'dic'} # key:value
b = {0:'python_dic'}
c = {'arr':[1,2,3,4]}
d = dict([
    ('name','python'),
    ('type','dic')
])
print(type(d),d)
f = dict(
    Name='Python', #이렇게 선언할때는 키값이 숫자가 될수 없음
    Type='Dic'
)
print(type(f),f)

## dictionary output
dic_out = dict(
    Name='Python',
    Type='Dic'
)
print(dic_out['Name'])
### print(dic_out['name']) #key값이 없으면 key error
print(dic_out.get('name')) #get 함수로 받아오면 없는 key값 이여도 key error가 나지 않는다

## add,edit dictionary
dic_add = dict(
    Name='Python',
    Type='Dic'
)
dic_add['Name'] = 'newPython' #기존에 존재하는 key값을 주면 value값을 수정한다
dic_add['How'] = 'add' #기존에 존재하지 않는 key값을 주면 추가 한다
dic_add['List'] = [1,2,3]
print(dic_add)

## len dictionary (key의 길이를 세줌)
dic_len = dict(
    Name='Python',
    Type='Dic'
)
print(len(dic_len))

## dictionary function (함수를 적용하면 부모 dictionary에 바로 반영된다)
print(dir(dic_len)) #__iter__존재하면 반복문 사용가능
'''
keys 키값들만 가져옴
values 값들만 가져옴
items 키,값 동시에 가져옴
pop 키와 값을 삭제해줌
popitem 임의로 key값 없이 값을 꺼내옴
update 값을 수정할때 사용
'''
dic_test = dict(
    Name='Python',
    Type='Dic',
    HOW='add',
    List=[1,2,3]
)
print(dic_test.keys())
print(list(dic_test.keys())) #dict_keys 값을 list로 type casting

print(dic_test.values())
print(list(dic_test.values())) #dict_values 값만 list로 type casting 

print(dic_test.items()) #tuple 형태로 반환
print(list(dic_test.items())) #각원소가 tuple형태인 list 반환

print(dic_test.pop('Name')) #꺼내서 바로 값으로 사용가능
print(dic_test)

dic_test = dict(
    Name='Python',
    Type='Dic',
    HOW='add',
    List=[1,2,3]
)

print(dic_test.popitem()) #꺼내서 바로 값으로 사용가능
print(dic_test.popitem())
print(dic_test.popitem())
print(dic_test.popitem())
print(dic_test)

dic_test = dict(
    Name='Python',
    Type='Dic',
    HOW='add',
    List=[1,2,3]
)

dic_test.update(Name = 'New Py')
print(dic_test)
temp = {'Name':'Origin Py'}
dic_test.update(temp)
print(dic_test)

## in operator
dic_test = dict(
    Name='Python',
    Type='Dic',
    HOW='add',
    List=[1,2,3]
)
print('Name' in dic_test)
print('type' in dic_test)