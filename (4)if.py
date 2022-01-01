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
