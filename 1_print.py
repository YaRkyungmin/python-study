# autor: YaRkyungmin
# 2021-12-27
# how to use Print Function

# basic output
print('Python Start!') #print문은 기본적으로 한줄 띄움
print("Python Start!")
print()
print("""Python Start!""")
print('''Python Start!''')

# seprator option
print('P', 'Y', 'T', 'H', 'O' , 'N', sep = '_')

# end option
print('Welcome to', end=' ')
print('Python')

# file option
import sys
print('file Python', file=sys.stdout) #ex) file = 'test.txt' 

# formating(d: 123, s: 'python', f: 1.23)
print('%s %s' %('one','two'))
print('{} {} {}'.format('123', 'python', '1.23'))
print('{1} {0}'.format('two','one'))

## %s
print('%10s' %('count'))
print('%10s' %('count123'))
print('{:>10}'.format('count'))
print('{:>10}'.format(1333))

print('%-10s' %('count'))
print('%-10s' %('count123'))
print('{:10}'.format('count')) #s 생략 가능

print('{:_>10}'.format('count'))
print('{:_<10}'.format('count'))
print('{:^10}'.format('count'))
print('{:_^10}'.format('center'))

print('%5s' %('longlongpython'))
###longlongpython
print('%.5s' %('longlongpython')) #공간이 없는것
###longl
print('{:10.5}'.format('longlongpython')) #공간이 있는것
###longl
print('{:>10.5}'.format('longlongpython')) 
###    longlo

## %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' %(42)) #d 생략 불가능
print('{:4d}' .format(42))

## %f
print('%f' %(3.14159242424))
print('{:f}'.format(3.14159242424)) #f 생략 불가능

print('%8.2f' %(333.1323))
print('%08.2f' %(333.1323)) #8자리중 빈자리를 0으로 채움
print('{:08.2f}'.format(333.1323))