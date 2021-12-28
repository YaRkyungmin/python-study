# autor: YaRkyungmin
# 2021-12-28
# Python DataType Number

# number datatype
'''
int 
float 
complex 복소수
'''

## number operator
'''
+
-
*
/
// : quotient
% : remainder
abs(x) : absolute value
pow(x, y) : x ** y
'''

## integer declare
'''
python은 얼마나 큰 숫자든 상관없이 선언 가능하다.
'''
test_variable = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(test_variable)

## automatic type casting
int_number = 2
float_number = 1.4

sum_number = int_number + float_number
mul_number = int_number * float_number
print(sum_number)
print(mul_number)
print(type(mul_number))
print(type(sum_number))

## number of type casting
int_number1 = 77
float_number1 = .4
float_number2 = .33
complex_number = complex(22)

print(int(float_number1))
print(int(float_number2))
print(float(int_number1))
print(type(complex_number))
print(complex(int_number1))
print(complex('2'))
print(int(True))
print(float(False))

## numerical arithmetic function(수치연산함수)
print(abs(-7))
x, y = divmod(100,8)
print(x,y)
print(pow(4,2),4**2)

## import math module
import math

x = 5.1
print(math.ceil(x)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)