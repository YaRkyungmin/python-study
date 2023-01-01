# autor: YaRkyungmin
# 2022-05-07
# Function Argument

# mutable Argument
'''
함수의 인자를 전달할 때 mutable한 객체를 전달하면 영향을 받는다
'''
def mutableOfFunction(mu_li):
    mu_li.append('add')
    print("mutableOfFunction:",mu_li)
    print(id(mu_li))
test_list = ['p','y','t','h','o','n']
mutableOfFunction(test_list)
print(f"test_list: {test_list}")
print(id(test_list))

## return
'''
return을 통해 mutable한 argument를 전달받아도 영향을 받는다
'''
def mutableOfFunction2(mu_li):
    mu_li.append('add')
    print("mutableOfFunction2:",mu_li)
    print(id(mu_li))
    return mu_li
test_list2 = ['p','y','t','h','o','n']
test_li = mutableOfFunction2(test_list2)
print(f"test_li: {test_li}")
print(id(test_li))

### solution
'''
리스트 슬라이싱을 통해 shallow copy를 하거나
copy 모듈을 통해 deep copy를 해서 사용한다
'''
def solutionOfFunction(re_list):
    copy_list = re_list[:]
    copy_list.append('add')
    return copy_list
sol_list = ['a','p','p','l','e']
reply_list = solutionOfFunction(sol_list)

print("sol_list",sol_list,id(sol_list))
print(reply_list,id(reply_list))

import copy as cafe
from turtle import pos
def solutionOfFunction2(re_list):
    copy_list2 = cafe.deepcopy(re_list)
    copy_list2.append('add')
    return copy_list2
sol_list2 = ['a','p','p','l','e']
reply_list2 = solutionOfFunction2(sol_list2)

print("sol_list2",sol_list2,id(sol_list2))
print(reply_list2,id(reply_list2))

## function argument default value
'''
function이 정의될때 한번 초기화 시킨다
호출될때마다 초기화 시키는것이 아니다
'''
def defaultOfFunction(a = 777):
    print(a)
defaultOfFunction(4)
defaultOfFunction()

'''
mutable한 객체를 default value로 문제가 발생
정의될때 한번만 초기화 하기 때문
'''
def defaultOfFunction2(a = []):
    a.append('p')
    print(a,id(a))
defaultOfFunction2()
defaultOfFunction2()
defaultOfFunction2()
defaultOfFunction2()

### solution
'''
None값일때만 리스트를 초기화
'''
def defaultOfFunction3(a = None):
    if a is None:
        a = []
    a.append('p')
    print(a,id(a))

defaultOfFunction3()
defaultOfFunction3()
defaultOfFunction3()
defaultOfFunction3()

# positional argument
'''
define한 인자 위치대로 대입
순서가 중요
'''
def positionalOfFuntion(a,b,c):
    print("positionalOfFuntion")
    print(f"position1: {a}")
    print(f"position2: {b}")
    print(f"position3: {c}")
positionalOfFuntion(2,3,65)

# keyword argument
"""
keyword argument를 이용하면 순서 없이 입력 가능
positional argument와 혼합하여 이용 가능 (positional, keyword)순으로 입력 해야한다.
"""
def keywordOfFuntion(a,b,c):
    print("keywordOfFuntion")
    print(f"position1: {a}")
    print(f"position2: {b}")
    print(f"position3: {c}")

keywordOfFuntion(10,c = 100, b = 1)

# unpacking
"""
* 
**

함수 내부에서 사용, 변수 대신 바로 사용 가능
함수 입력,정의 모두 사용가능
함수 입력시 사용: 인자 갯수 제한
함수 정의시 사용: 인자 갯수 무제한, 
(positional arg, *args, **args) 순서대로 정의해야함
"""
def unpackingOfFunction(a,b,c):
    print("unpackingOfFunction")
    print(f"position1: {a}")
    print(f"position2: {b}")
    print(f"position3: {c}")

test =[1,2,30]
unpackingOfFunction(*test)
unpackingOfFunction(*(2,3,5))

def unpackingOfFunction2(a,b,c,*args):
    print("unpackingOfFunction2")
    print(f"a: {a}, b: {b}, c: {c}")
    for i,v in enumerate(args):
        print(f"index: {i}, value: {v}")

word = 1 << 10 - 1
unpackingOfFunction2(1,2,3,*format(word,'04b'),777,77)

def unpackingOfFunction3(**args):
    print("unpackingOfFunction3")
    print("argsID", id(args))
    for i,v in enumerate(args):
        print(f"index: {i}, key: {v}, value: {args[v]}, id: {id(args[v])}")

dic_test = {'name':'kyungmin', 'age':'27', 'hobby':'climing'}
print("dic_testID",id(dic_test))
for i,v in enumerate(dic_test):
    print(f"index: {i}, dic_testID: {id(dic_test[v])}")
unpackingOfFunction3(**dic_test)