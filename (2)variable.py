# autor: YaRkyungmin
# 2021-12-27
# Python Variable

# basic declare
'''
_ 혹은 영문자로 시작해야 한다.
숫자로 시작할 수 없다
특수문자(+,-,%,^,%등)은 사용할 수 없다.
변수 이름에 공백이 있으면 안 된다 (보통 _로 이어줌)
'''
n = 500
print(n)
print(type(n))

# simultaneous declaration
x = y = z = 300
print(x,y,x) 

# redeclaration
a = 12
a = 'apple'
print(a)
print(type(a))

# Object References
## ex) print(300)
## 변수 값 할당 상태
## 1. 타입에 맞는 오브젝트 생성
## 2. 값 생성
## 3. 콘솔 출력
print(200)
print(int(200))

# id(identity) confirm
m = 800
n = 400
print(id(m))
print(id(n))
z = 400 #효율적으로 하나의 인스턴스(instance)를 사용, 같은 오브젝트를 참조
print(id(z) == id(n))

# how to declare Variable
## Camel Case : numberOfCollegeGraduates -> Method declare
## Pascal Case : NuberOfCollegeGraduates -> Class declare
## Snake Case : nuber_of_college_graduates -> Variable declare

# do not use reserved words
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""