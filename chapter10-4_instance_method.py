# autor: YaRkyungmin
# 2023-01-01
# Instance Method

#instance method
'''
일반 method 정의
인스턴스 층에서 method를 호출하면 인스턴스를 넘겨준다
'''

class Dog:
    numbersOfDog = 0
    def __init__(self,species,age,numbersOfStep):
        Dog.numbersOfDog += 1
        self.species = species
        self.age = age
        self.numbersOfStep = numbersOfStep
    def __del__(self):
        Dog.numbersOfDog -= 1
    def explain(self):
        print(f'Specis : {self.species}, age : {self.age}, step : {self.numbersOfStep}')
    def walk(self,step):
        self.numbersOfStep += step

july = Dog('poodle',13,0)
print(Dog.numbersOfDog)
july.explain()
july.walk(100)
july.explain()