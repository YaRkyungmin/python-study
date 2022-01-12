# autor: YaRkyungmin
# 2022-01-04
# Python Function

# Function
'''
코드 간결화
코드 재사용성
코드 안정성
코드 모듈성

Python은 해석 된 언어이므로 하향식 접근 방식 
Python은 정적 진입 점이없고 소스 코드가 순차적으로 실행
Python의 메서드는 수동으로 호출해야함

def function_name(parameter):
    code
'''

## return value
'''
리턴 받을 수 있는 datatype
variable
tuple
list
dic
set
'''
def value_function(s):
    return 'a'+ s
print(value_function('pple'))

## multi return value
def mul_value(x):
    x1 = x * 10
    x2 = x * 20
    x3 = x * 30
    return x1,x2,x3

x, y, z = mul_value(10)
print(x,y,z)

## *args(unpacking)
'''

'''
def args_func(*args):
    for i, v in enumerate(args): #enumerate 인덱스와 원소로 이루어진 tuple을 반환 한다
        print('Result : {} {}'.format(i,v))


args_func('Lee')

def args_func(*args):
    for i, v in enumerate(args,start=1): 
        print('Result : {} {}'.format(i,v))

args_func('Python')

