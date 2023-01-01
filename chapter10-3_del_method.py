# autor: YaRkyungmin
# 2023-01-01
# Del Method

#del
'''
객체가 소멸할때 자동으로 호출되는 함수
'''
class Warehouse:
    stock_numbers = 0

    def __init__(self):
        Warehouse.stock_numbers +=1
    def __del__(self):
        Warehouse.stock_numbers -=1

stuff1 = Warehouse() 
stuff2 = Warehouse()
del stuff1
del stuff2
print(Warehouse.stock_numbers)