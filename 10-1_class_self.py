# autor: YaRkyungmin
# 2023-01-01
# Self

#self
'''
self는 instance를 넘겨 받는다.
'''
class SelfTest:
    def func1():
        print("Func1 called") 
    def func2(self):
        print(id(self))
        print(self)
        print("Func2 called")

##instance method
t = SelfTest()

### t.func1() #error_func1은 넘겨받는 인자가 없는데 instance를 넘겨받아서 error 발생, 매서드 호출 시 무조건 인스턴스를 인자로 넘겨줌
print(id(t))
t.func2()

##class method
SelfTest.func1
SelfTest.func2(t)