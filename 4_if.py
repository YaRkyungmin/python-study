# autor: YaRkyungmin
# 2022-01-01
# Python Conditional Statement

# if
print(type(True)) # 0이 아닌 수, "abc", [1,2,3,..]
print(type(False)) # 0, '', [], (), {}
print(True * 8)
print(False * 2)

ex = []
if ex:
    print("success") #indentation == 4's space
else:
    print("fail")

ex2 = [0]
if ex2:
    print(type(ex2),"success")
else:
    print("fail")

ex3 = ()
if ex and ex2:
    print("success")
    print(not True)
elif ex or ex3:
    print("success2")
elif not ex3:
    print("success3")
    print(not False)
else:
    print("fail")

## priority
'''
산술(+, -, /, *) > 관계(==, >=) > 논리(and, or, not)
'''
print('priority:',3+12 > 1+1)
print('priority:', 5+10 > 3 and 7+3 == 10)
print('priority:', 5+10 > 0 and not 7 + 3 == 10)

## in, not in
ex1 = [10,20,30]
ex2 = {70,80,90,100}
ex3 = {'name':'py', 'test':'thon'}
ex4 = (10,12,14)

print(10 in ex1)
print(60 in ex2)
print('name' not in ex3)
print('py' in ex3.values()) #values를 함수를 사용하면 key값이 아닌 values에서 검색가능
print(10 in ex4)