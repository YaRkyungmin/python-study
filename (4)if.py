# autor: YaRkyungmin
# 2022-01-01
# Python Conditional Statement

# if
print(type(True)) # 0이 아닌 수, "abc", [1,2,3,..]
print(type(False)) # 0, '', [], (), {}

ex = []
if ex:
    print("success")
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
산술 > 관계 > 논리
'''