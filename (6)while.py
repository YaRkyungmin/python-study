# autor: YaRkyungmin
# 2022-01-03
# Python While Statement

# while
'''
while <expr>:
    <statement(s)>
'''
test = [1,2,3,4]
while test:
    print(test.pop())

## break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

## continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

## while else statement (while문이 중간에 끊기지 않고 실행됐으면 else문이 실행된다, break문과 함께 사용)
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 4:
        break
else:
    print('else 실행')
print('while else test_1 end')

n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print('else 실행')
print('while else test_2 end')