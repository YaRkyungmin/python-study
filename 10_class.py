# autor: YaRkyungmin
# 2023-01-01
# Python Class

#class
'''
OOP
object, class, instance
method
reusable
'''
##class declare
class Dog(object): 
    pass

class Cow():
    pass

class Cat:
    pass

class Animal: #object 상속
    class_name = 'Animal' #class variable 또는 클래스 속성
    def __init__(self, A, B): #초기화/인스턴드 속성(기본문법)
        self.species = A
        self.name = B

print(Animal)

##class instance
dog_kang = Animal("Dog", 'kang')
cow_kang = Animal("Cow", 'kang')
dog_kang2 = Animal("Dog", 'kang') #값이 같아도 다른 객체
print(f'id dog_kang: {dog_kang}, id cow_kang: {cow_kang}, id dog_kang2: {dog_kang2}')
print('----------------------')

##name space
'''
object를 instance화 할때 저장된 공간
'''
print(f'dog_kang ns: {dog_kang.__dict__}')
print(f'Animal ns: {Animal.__dict__}')
print('----------------------')

##class attribute
'''
직접 접근 가능, 공유
클래스 속성을 인스턴스 층에서 건드리면 클래스속성이 인스턴스 속성이 됨=name space에 추가가 됨(이떄, 얕은 복사가 일어남 그래서 리스트는 계속 공유하지만 변수는 공유하지 않는다)
인스턴스 층에서 건드리기 전에는 name space에 속성 값이 없으면 클래스 name space에서 값을 찾음
'''
kang = [1,2,3]
won = kang
won.append(100)
print(f'kang: {kang}')

import copy as cafe #깊은 복사 하는법
won2 = cafe.deepcopy(kang)
won2.append(1000)
print(f'kang: {kang}')

test = 100
test2 = 100 #test, test2는 동일 메모리 주소
test2 += 1 #test2에 덧셈과 동시에 다른 메모리 주소값으로 바뀜

print(f'Animal.class_name : {Animal.class_name}')
print('----------------------')
dog_kang.class_name = 'strange_Animal' #클래스 속성을 인스턴스 층에서 건드리면 클래스속성이 인스턴스 속성이 됨.
print(f'Animal.class_name : {Animal.class_name}')
print(f'dog_kang.class_name : {dog_kang.class_name}')
print(f'dog_kang ns: {dog_kang.__dict__}')
print('----------------------')
Animal.class_name = 'change_Animal'
print(f'Animal.class_name : {Animal.class_name}')
print(f'dog_kang.class_name : {dog_kang.class_name}')
print(f'cow_kang.class_name : {cow_kang.class_name}')
print('----------------------')

##instance attribute
'''
객체마다 별도 존재
'''
print(dog_kang.species)

