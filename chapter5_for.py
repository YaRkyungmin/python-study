# autor: YaRkyungmin
# 2022-01-02
# Python For Statement

# for
'''
for in <collection>
    <Loop body>
'''

## range(start,stop,step)
for i in range(2,10,2):
    print(i)

## iterables datatype (str, list, tuple, set, dic) iterable 자료형은 for문에서 사용 가능
'''
*iterable return function
range
reversed
enumerate
filter
map
zip
'''
str_iter = 'striter'
for i in str_iter:
    print(i,end=' ')
print()

list_iter = [1,2,3,4,5]
for i in list_iter:
    print(i,end=' ')

tuple_iter = (1,2,3)
for i in tuple_iter:
    print(i,end=' ')
print()

dic_iter = dict(
    Name = 'py',
    Test = 'thon'
)
for i in dic_iter:
    print(i,end=' ')
print()
for key in dic_iter:
    print(dic_iter.get(key),end='')
print()
for value in dic_iter.values():
    print(value,end='')
print()

str_reversed = 'apple'
print("reverse:",reversed(str_reversed)) #indentity값이 나옴
print("reverse:",list(reversed(str_reversed)))
print("reverse:",tuple(reversed(str_reversed)))
print("reverse:",set(reversed(str_reversed))) #순서가없음 랜덤으로 계속 나옴 집합은 순서 X

## break
for_break = [1,2,3,4,100,5,6,7,8,9]

for num in for_break:
    if num == 100:
        print("found")
        break
    else:
        print("not",end = ' ')

## continue
for_continue = ['1',12,3,45,True,4.3,complex(4)]

for v in for_continue:
    if type(v) is bool:
        continue
    print(type(v))

## for else statement (for문이 중간에 끊기지 않고 실행됐으면 else문이 실행된다, break문과 함께 사용)
for_else = [1,2,3,4,100,5,6,7,8,9]

for num in for_else:
    if num == 1000:
        print("found")
        break
else:
    print('Not found 1000')