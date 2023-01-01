# autor: YaRkyungmin
# 2023-01-01
# Python Module

# module
'''
변수,메서드,클래스 등 파이썬 구성 요소 들을 모아놓은 file
'''

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
import testfunction #import할때 __name__=__main__ 으로 testfunction.py을 한번 실행함
print(__name__)
testfunction.hello() #__name__=__testfunction__ 으로 testfunction.py을 한번 실행함
import testfunction #같은 module을 import하면(import할때 메모리에 계속 기억하고 있음) 다시 실행되지 않는다

## sys module
import sys
input = sys.stdin.readline
'''
propmt 출력여부
readline은 한번에 읽어 버퍼에 저장
input은 값을 입력할 때마다 버퍼에 저장
'''
print(list(sys.stdin.readline())) #개행문자까지 입력받음
print(list(sys.stdin.readline().split())) #제거

print(sys.path)