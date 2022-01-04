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