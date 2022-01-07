# autor: YaRkyungmin
# 2021-12-27
# Python DataType

#datatype
'''
int 
float 
complex 복소수
bool (True:1 , False:0)
str (sequence types) #sequence type 은 in 연산 사용 가능
list (sequence types)
tuple (sequence types)
set
dict
'''

## is function 자료형을 비교해줄때는 is funciton을 사용
test_str = 1
print(type(test_str) is str)
print(type(test_str) is bool)
print(type(test_str) is int)

## mutable datatype
'''
list
set
dict
'''
a= [1,2,3]
print(id(a))
a[0] = 5
print(id(a))
## immutable datatype
'''
bool
int
float
tuple
'''