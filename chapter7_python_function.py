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

## *args, **kwargs (unpacking)
'''
* : 입력 값을 들어오는 갯수와 상관없이 튜플형태를 반환해줌
** : 입력 값에 들어오는 갯수와 상관없이 딕셔너리 형태를 반환해줌
'''
def args_func(a,*args,**kwargs):
    print("args_func")
    print(a)
    for i, v in enumerate(args): #enumerate 인덱스와 원소로 이루어진 tuple을 반환 한다
        print('Result : {} {}'.format(i,v))
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
args_func(1,2,'Lee',name1 = 'P', name2 = 'Y',name3 = 'T')

## 중첩 function
def function_out(num):
    def function_in(num): #function안에서 호출된 function을 밖에서 선언하면 error 발생
        print(num)
    print("In func")
    function_in(num+100)

function_out(100)
### function_in(100) #error 발생

print("-----------------------")
## lambda
'''
메모리 절약
가독성 향상
코드 간결
function : 객체생성 -> resource(memory) 할당
lambda : 즉시실행 -> Heap 할당 초기화 -> memory 초기화
많이 사용시 가독성 감소
'''
def def_function (x,y):
    return x*y

lambda_funcution = lambda x, y:x*y #lambda_function과 같은 뜻

mul_function = def_function #일반 함수 할당
print(mul_function(10,10))

print(lambda_funcution(10,10))

def multilambda_fun(x,y,func):
    print(x * y * func(100,100))

multilambda_fun(10,20,def_function)
multilambda_fun(10,20,lambda x, y : x*y)

print("-------------------")
## type annotation_variable
'''
실질적으로 어떠한 제약 사항도 강요되지 않음
Mypy 도구를 이용하여 인터프리터가 체크하지못한 type버그를 찾을 수 있음
'''
name: str = "John Doe"
age: int = 25
emails: list = ["john1@doe.com", "john2@doe.com"]
address: dict = {
  "street": "54560 Daugherty Brooks Suite 581",
  "city": "Stokesmouth",
  "state": "NM",
  "zip": "80556"
}
print(name, age, emails, address)

## type annotation_function
'''
실질적으로 어떠한 제약 사항도 강요되지 않음
mypy를  사용하면 type error를 어느정도 잡을 수 있음
'''
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)