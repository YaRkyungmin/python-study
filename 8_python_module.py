# autor: YaRkyungmin
# 2022-01-05
# Python Module

## main function declare
'''
런타임 중에 또는 프로그램이 실행될 때 시스템을 작동하여 자동으로 함수를 호출하는 데 도움이되는 특수 함수
__name__ : 현재 모듈의 이름을 담고있는 내장 변수
'''
def main(s): #prameter지정후 prameter가 없을 경우는 error발생
     print(s)
if __name__ == "__main__" :
     main("This is main Function")

## import module
import testfunction #import할때 testfunction을 한번 실행함
print(__name__)
testfunction.hello()
import testfunction #같은 module을 import하면(import할때 메모리에 계속 기억하고 있음) 다시 실행되지 않는다