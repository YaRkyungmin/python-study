# autor: YaRkyungmin
# 2021-12-28
# Python DataType String

# string datatype
str1 = "Python"
str2 = 'Pyhon'
str3 = """Python"""
str4 = '''P y t h o n'''

## 빈문자열 생성
str5 = '' 
str6 = str()

print(len(str4))
print(type(str6))

## escape sequence
print('I\'m P\ny\tt\\h\141on')
'''
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : \ 뒤에 8진수 숫자를 지정하여 ASCII 코드의 문자 표현
'''

## row string
raw_str = r'D:\Python Test\test1' #\뒤에 문자를 escape 문자를 사용하지 않고 그대로 받아들임.
print(raw_str)

## multi line input (역슬래시를 사용)
multi_str = \
'''
P
Y
T
H
O
N
'''
multi_str2 = \
    'a'\
    'p'\
    'p'\
    'l'\
    'e'
print(multi_str)
print(multi_str2)

## str operator
'''
+
,
*
in
not in
'''
str_01 = "Python"
str_02 = "APPLE"

print(str_01 * 3)
print(str_01 + str_02)
print(str_01,str_02) #공백후 출력
print('y' in str_01)
print('z' in str_01)
print('p' not in str_02)

## str of type casting
print(str(98),type(str(98)))
print(str(10.1))
tc_str = True
print(type(str(tc_str)))

## 문자열 함수
'''
capitalize 첫번째 문자를 대문자로 변경
replace 지정문자를 모두 찾아서 교체해줌
endswith 마지막문자가 조건대로 끝나는지를 판별
sorted 문자열을 넣어주면 리스트형태로 반환
split 특정 단어기준으로 분리하여 리스트로 반환
upper 모든 문자열을 대문자로 변경
lower 모든 문자열을 소문자로 변경
isalnum 0-9숫자와 a-z알파벳으로만 구성돼있는지 확인해줌
join
startswith
count
isalpha
'''
cp_str = 'python'
ew_str = 'python!'
re_str = 'python python python'
st_str = 'pythonpython'
sp_str = 'p y th o n'
up_str = 'python'
lo_str = 'PYTHON'
is_str = 'python123!!@'
is_str1 = 'python123'
print("capitalize:", cp_str.capitalize()) 
print("endswith:", ew_str.endswith("!"))
print("replace:", re_str.replace('python','replace'))
print("sorted:", sorted(st_str))
print("split:",sp_str.split(' '))
print("upper:",up_str.upper())
print("lower:",lo_str.lower())
print("isalnum:",is_str.isalnum())
print("isalnum:",is_str1.isalnum())

## 반복(시퀀스-순서가있는 배열형태) 
sq_str = 'im squence'

print(dir(sq_str)) #__iter__: 반복할수 있다는 뜻
for i in sq_str:
    print(i)

## slicing 
sl_str = 'good python very nice'
print(len(sl_str))
print(sl_str[3:6]) #3,4,5
print(sl_str[:3])
print(sl_str[0:7])
print(sl_str[0:len(sl_str)])
print(sl_str[0:len(sl_str):2])
print(sl_str[-10:])
print(sl_str[-10:-1]) #뒤의 인자 -1을 해주는데 까지
print(sl_str[::2])
print(sl_str[::-1])#뒤에서부터
print(sl_str[100:200]) #sliching 할때는 인덱스 범위를 벗어나도 out of range error가 나지 않는다. 

## ASCII code : ord()함수, chr()함수
a = 'z'
print(ord(a))
print(chr(122))
