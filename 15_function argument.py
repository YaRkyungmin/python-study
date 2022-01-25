# autor: YaRkyungmin
# 2022-01-12
# Function Argument

# mutable Argument
'''
함수의 인자를 전달할 때 mutable한 객체를 전달하면 영향을 받는다
'''
def mutableOfFunction(mu_li):
    mu_li.append('add')
    print(mu_li)
    print(id(mu_li))
test_list = ['p','y','t','h','o','n']
mutableOfFunction(test_list)
print(test_list)
print(id(test_list))

## return
'''
return을 통해 mutable한 argument를 전달받아도 영향을 받는다
'''
def mutableOfFunction2(mu_li):
    mu_li.append('add')
    print(mu_li)
    print(id(mu_li))
    return mu_li
test_list2 = ['p','y','t','h','o','n']
test_li = mutableOfFunction2(test_list2)
print(test_li)
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

print(sol_list,id(sol_list))
print(reply_list,id(reply_list))

import copy as cafe
def solutionOfFunction2(re_list):
    copy_list2 = cafe.deepcopy(re_list)
    copy_list2.append('add')
    return copy_list2
sol_list2 = ['a','p','p','l','e']
reply_list2 = solutionOfFunction2(sol_list2)

print(sol_list2,id(sol_list2))
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
mutable한 객체를 초기화 시키면 문제가 발생
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