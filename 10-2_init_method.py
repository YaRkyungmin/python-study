# autor: YaRkyungmin
# 2023-01-01
# Init Method

#init
'''
객체를 초기화할때 자동으로 호출되는 함수
'''
class Warehouse:
    stock_numbers = 0

    def __init__(self):
        Warehouse.stock_numbers +=1

stuff1 = Warehouse() #인스턴스
stuff2 = Warehouse #Wahrehouse 클래스를 복사
stuff3 = stuff2()

print(Warehouse.stock_numbers)